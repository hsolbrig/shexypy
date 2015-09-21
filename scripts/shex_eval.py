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
from _collections_abc import Iterable
import sys
import os
import argparse

from rdflib import URIRef, Graph

from antlr4.InputStream import InputStream

from pyxb.utils.domutils import StringToDOM

_curdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(_curdir, '..'))

from shexypy.schema.ShEx import CreateFromDOM, ShapeLabel
from shexypy.shexyinterpreter.ShapeInterpreter import ShapeInterpreter
from shexypy.utils.xmlutils import prettyxml
from shexypy.utils.manifest import ShExManifest, ShExManifestEntry
from scripts.shex_parser import do_parse


def build_argparser() -> argparse.ArgumentParser:
    """ Construct a basic argument parser.  This is a separate module so main specific parameters
    can be added separately from the parse specific arguments
    :return: argument parser
    """
    parser = argparse.ArgumentParser(description="Run ShExDoc parser")
    parser.add_argument("-i", "--infile", help="Interpretation file.")
    parser.add_argument("-g", "--graph", help="Name of file containing the graph")
    parser.add_argument("-f", "--format", help="Graph file format", default="turtle")
    parser.add_argument("-p", "--print", help="Print parsed XML", action="store_true")
    parser.add_argument("-s", "--start", help="Staring shape label")
    parser.add_argument("-n", "--node", help="Focus node in graph")
    parser.add_argument("-m", "--manifest", help="Name of manifest file")
    parser.add_argument("-t", "--test", help="Entry in the manifest file")
    return parser


def parse_args(argparser: argparse.ArgumentParser, args: list) -> argparse.Namespace:
    """ Parse the input arguments
    :return: Parsed input arguments
    """
    opts = argparser.parse_args(args)
    if opts.manifest:
        if opts.infile or opts.graph or opts.start or opts.node:
            print("Cannot specify individual files and a manifest", file=sys.stderr)
            return None
    elif not (opts.infile and opts.graph and opts.node):
        print("Input schema, graph and start node must be specified")
        return None
    elif opts.test:
        print("Cannot supply a manifest entry without a manifest file")
        return None
    return opts


class memory_file:
    def __init__(self):
        self._buffer = ""

    def write(self, val):
        self._buffer += val

    def read(self):
        return self._buffer


def eval_entry(shex: str, start_shape: str, start_node: str, g: Graph, opts: argparse.Namespace):
    schema = do_parse(InputStream(shex))
    schema_xml = prettyxml(schema.to_dom())
    if opts.print:
        print(schema_xml)
    schema_dom = StringToDOM(schema_xml)
    schema = CreateFromDOM(schema_dom)
    si = ShapeInterpreter(schema, schema_dom, g)
    # TODO: Kludge to fix a bug in the manifest itself
    if str(start_shape) not in si._shapes:
        start_shape = str(start_shape).split('/')[-1]
    return si.i_shape(URIRef(start_node) if start_node else None, ShapeLabel(start_shape))


def eval_manifest_entry(e: (str, Iterable), opts: argparse.Namespace):
    print("Evaluating: %s" % e[0])
    mes = e[1]
    for me in mes:
        print("   Entry: %s - " % me.entryuri, end='')
        rslt = eval_entry(me.schema, me.start_shape, me.subject_iri, me.instance(fmt=opts.format), opts)
        print("PASS" if rslt == me.should_pass else "FAIL")


def main(argv: list):
    sys.path.append(os.path.join(_curdir, '../shexypy/shexyparser/parser'))
    sys.path.append(os.path.join(_curdir, '../shexypy/shexyparser/parser_impl'))
    parser_args = build_argparser()
    opts = parse_args(parser_args, argv)
    if not opts:
        sys.exit(0)
    if opts.manifest:
        mf = ShExManifest(opts.manifest, fmt=opts.format)
        if not opts.test:
            for e in sorted(mf.entries.items(), key=lambda x: x[0]):
                eval_manifest_entry(e, opts)
        else:
            if opts.test in mf.entries:
                eval_manifest_entry((opts.test, mf.entries[opts.test]), opts)
            else:
                print("%s not found in manifest" % opts.test)
    else:
        indoc = open(opts.infile).read()
        schema_dom = StringToDOM(indoc)
        schema = CreateFromDOM(schema_dom)
        if opts.print:
            print(prettyxml(schema))
        g = Graph()
        g.parse(opts.graph, format=opts.format)
        if ShapeInterpreter(schema, schema_dom, g).i_shape(URIRef(opts.node), ShapeLabel(opts.start)):
            print("*** Success ****")

if __name__ == '__main__':
    main(sys.argv[1:])
