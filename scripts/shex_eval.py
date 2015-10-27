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
from shexypy.utils.manifest import ShExManifest
from scripts.shex_parser import do_parse


def build_argparser() -> argparse.ArgumentParser:
    """ Construct a basic argument parser.  This is a separate module so main specific parameters
    can be added separately from the parse specific arguments
    :return: argument parser
    """
    parser = argparse.ArgumentParser(description="Run ShExDoc parser, either against a manifest or an individual file")
    parser.add_argument("-i", "--infile", help="Interpretation file.")
    parser.add_argument("-if", "--infile_format", help="Interpretation file format",
                        choices=("xml", "shex"), default="shex")
    parser.add_argument("-g", "--graph", help="Name of file containing the graph")
    parser.add_argument("-gf", "--graph_format", help="Graph file format", default="turtle")
    parser.add_argument("-p", "--print", help="Print parsed XML", action="store_true")
    parser.add_argument("-ss", "--start_shape", help="Staring shape label")
    parser.add_argument("-fn", "--focus_node", help="Focus node in graph")
    parser.add_argument("-m", "--manifest", help="Name of manifest file")
    parser.add_argument("-mf", "--manifest_format", help="Manifest file format", default="n3")
    parser.add_argument("-me", "--manifest_entry", help="Name of entry to test in the manifest file")
    return parser


def parse_args(argparser: argparse.ArgumentParser, args: list) -> argparse.Namespace:
    """ Parse the input arguments
    :return: Parsed input arguments or None if there is a parameter error
    """
    opts = argparser.parse_args(args)
    if opts.manifest:
        if opts.infile or opts.graph or opts.start_shape or opts.focus_node:
            print("Cannot specify input file, graph, shape or focus node if using a manifest", file=sys.stderr)
            return None
    elif not (opts.infile and opts.graph and opts.focus_node):
        print("Either a manifest or an input schema, graph and focus node must be specified")
        return None
    elif opts.manifest_entry:
        print("Cannot supply a manifest entry without a manifest file")
        return None
    return opts


def eval_shexml(shex_xml: str, start_shape: str, focus_node: str, g: Graph, opts: argparse.Namespace) -> bool:
    """ Evaluate the shex Schema instance against the start shape and focus node
    :param shex_xml: ShExML representation of ShEx node
    :param start_shape: name of starting shape in schema
    :param focus_node: uri of focus node in graph
    :param g: object graph
    :param opts: additional options
    :return:
    """
    if opts.print:
        print(prettyxml(shex_xml, toxml=False))
    schema_dom = StringToDOM(shex_xml)
    schema = CreateFromDOM(schema_dom)
    si = ShapeInterpreter(schema, schema_dom, g)
    # TODO: Kludge to fix a bug in the manifset where ?
    if str(start_shape) not in si._shapes:
        start_shape = str(start_shape).split('/')[-1]
    return si.i_shape(URIRef(focus_node) if focus_node else None, ShapeLabel(start_shape))


def eval_manifest_entry(name: str, entries: Iterable, opts: argparse.Namespace) -> None:
    """ Evaluate a manifest entry
    :param name: name of the manifest entry
    :param entries: actual manifest entries (there can be more than one per name...)
    :param opts: function options
    """
    print("Evaluating: %s" % name)
    for entry in entries:
        print("   Entry: %s - " % entry.entryuri, end='')
        parsed_shex = do_parse(InputStream(entry.schema))
        parsed_xml = prettyxml(parsed_shex.to_dom())
        rslt = eval_shexml(parsed_xml, entry.start_shape, entry.subject_iri,
                               entry.instance(fmt=opts.graph_format), opts)
        print("PASS" if rslt == entry.should_pass else "FAIL")


def eval_manifest(manifest_file: str, opts: argparse.Namespace) -> None:
    """ Evaluate an entire manifest or a single entry within
    :param manifest_file: name of the manifest file
    :param opts: function arguments
    """
    mf = ShExManifest(manifest_file, fmt=opts.manifest_format)
    if not opts.manifest_entry:     # All entries
        for k, v in sorted(mf.entries.items(), key=lambda x: x[0]):
            eval_manifest_entry(k, v, opts)
    else:                           # Single entry
        if opts.manifest_entry in mf.entries:
            eval_manifest_entry(opts.manifest_entry, mf.entries[opts.manifest_entry], opts)
        else:
            print("%s not found in manifest" % opts.manifest_entry)


def eval_input_file(opts: argparse.Namespace) -> None:
    """ Evaluate an input XML or ShExC file
    :param opts: function arguments
    """
    with open(opts.infile) as inp_file:
        if opts.infile_format == "shex":
            parsed_shex = do_parse(InputStream(inp_file.read()))
            parsed_xml = prettyxml(parsed_shex.to_dom())
        else:
            parsed_xml = inp_file.read()
    g = Graph()
    g.parse(opts.graph, format=opts.graph_format)
    print("*** " +
          ("Success" if eval_shexml(parsed_xml, opts.start_shape, opts.focus_node, g, opts) else "NOMATCH") + "***")


def main(argv: list):
    sys.path.append(os.path.join(_curdir, '../shexypy/shexyparser/parser'))
    sys.path.append(os.path.join(_curdir, '../shexypy/shexyparser/parser_impl'))

    parser_args = build_argparser()
    opts = parse_args(parser_args, argv)
    if not opts:
        sys.exit(0)

    if opts.manifest:
        eval_manifest(opts.manifest, opts)
    else:
        eval_input_file(opts)


if __name__ == '__main__':
    main(sys.argv[1:])
