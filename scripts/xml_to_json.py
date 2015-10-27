# -*- coding: utf-8 -*-
# Copyright (c) 2015, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the <ORGANIZATION> nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
import os
import sys
import argparse
import json
from pyxb.utils.domutils import *

from dirlistproc.DirectoryListProcessor import DirectoryListProcessor
import re

_curdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(_curdir, '..'))

from shexypy.shexyconverter.json_converter import ShExSchema
from shexypy.utils.dict_compare import dict_compare


failing_tests = {'_all_header.xml': "Not actually part of the test suite"}


def to_json(infile: str, outfile: str, opts) -> bool:
    """ Convert infile (ShEx Schema XML) into S-JSON and save or print the results
    :param infile: Name of input file.  Use sys.stdin if absent
    :param outfile: Name of output file.  Use sys.stdout if absent
    :param opts: Parser options, which include the compare directory
    :return: True if conversion was successful (and compared if opts.comparedir)
    """
    if not infile:
        print("Enter Schema XML to parse:")
        print()
    else:
        print("FILE: %s" % infile)
    xml_dom = StringToDOM(open(infile, encoding='utf-8').read() if infile else sys.stdin.read())
    dict_schema = ShExSchema(xml_dom).json
    json_schema = json.dumps(dict_schema, indent=4)
    if outfile:
        open(outfile, 'w').write(json_schema)
    else:
        print(json_schema)
    if opts.comparedir:
        return compare_output(opts, dict_schema, outfile)
    return True


def compare_output(opts: argparse.Namespace, dict_schema: dict, outfile: str) -> bool:
    compare_file = os.path.join(opts.comparedir, os.path.split(outfile)[1])
    try:
        json_dict = json.loads(open(compare_file, encoding='utf-8').read())
    except FileNotFoundError:
        print("**** File not found: %s" % compare_file)
        return False
    dc_result, match_result = dict_compare(dict_schema, json_dict, d1name="Input", d2name="Expected",
                                           filtr=compare_filter)
    if not dc_result:
        print("FILE: %s" % os.path.split(outfile)[1], file=sys.stderr)
        print(match_result, file=sys.stderr)
    return dc_result

ignore_order = False


def compare_filter(kv1: (str, object), kv2: (str, object)) -> bool:

    def ks(de):
        return list(de.keys())[0]

    def node_name(e):
        return e[0].split('.')[-1]

    def is_bnode(e):
        return e.startswith("_:")

    def is_numeric(v):
        return re.search(r'\^\^http://www.w3.org/2001/XMLSchema#decimal$', v) or \
               re.search(r'\^\^http://www.w3.org/2001/XMLSchema#double$', v) or \
               re.search(r'\^\^http://www.w3.org/2001/XMLSchema#decimal$', v)

    def numeric_value(v):
        return float(re.sub(r'"(.*)"\^\^.*', r'\1', v))

    def has_lang(v):
        return re.search(r'"@[a-zA-Z-]+', v)

    def lang(v):
        return re.sub(r'"@(.*)', r'\1', v).lower()

    def comp_values(v1, v2):
        return (is_numeric(v1) and is_numeric(v2) and numeric_value(v1) == numeric_value(v2)) or \
               (has_lang(v1) and has_lang(v2) and lang(v1) == lang(v2)) or v1 == v2

    # All BNODES match
    if (not kv2 and is_bnode(kv1[0])) or (not kv1 and is_bnode(kv2[0])):
        return True
    if kv1 and kv2:
        if is_bnode(kv1[0]) and is_bnode(kv2[0]):
            return True
        if node_name(kv1) in ["reference", "start"] and node_name(kv1) == node_name(kv2) \
                and is_bnode(kv1[1]) and is_bnode(kv2[1]):
            return True
        # Semantic Actions are now lists and the target isn't yet updated:
        if kv1[0].split('.')[-1] in ["semAct", "startAct"] and kv2[0] == kv1[0]:
            # This fails because kv2 is unordered
            return sorted(kv1[1], key=ks) == sorted([{k: v} for k, v in kv2[1].items()], key=ks)
        if node_name(kv1) == 'values' and node_name(kv1) == node_name(kv2) and \
                not (isinstance(kv1[1], dict) or isinstance(kv1[1][0], dict)):
            return all([comp_values(v1, v2) for v1, v2 in zip(kv1[1], kv2[1])])
        if isinstance(kv1[1], list) and isinstance(kv2[1], list):
            return ignore_order and len(kv1[1]) == len(kv2[1]) and all(e in kv2[1] for e in kv1[1])

    return False


def main(argv: list):

    def add_args(parser: argparse.ArgumentParser):
        parser.add_argument("-cd", "--comparedir", help="Directory of target JSON")
        parser.add_argument("-io", "--ignoreorder", help="Ignore list ordering when validating", action="store_true")

    def get_order(opts: argparse.Namespace):
        global ignore_order
        ignore_order = opts.ignoreorder

    dlp = DirectoryListProcessor(argv, "ShEx to XML Parser", '.xml', '.json', addargs=add_args, postparse=get_order)
    nfiles, npassed = dlp.run(to_json, file_filter=lambda fn: fn not in failing_tests)
    print(file=sys.stderr)
    print("***** " + ("Success" if nfiles == npassed else "FAILURE") + " *****", file=sys.stderr)
    print("\t%d File%s Processed" % (nfiles, '' if nfiles == 1 else 's'), file=sys.stderr)
    print("\t%d Error%s" % (nfiles - npassed, '' if nfiles - npassed == 1 else 's'), file=sys.stderr)


if __name__ == '__main__':
    main(sys.argv[1:])
