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
import sys
import argparse

from rdflib import URIRef, Graph

from shexypy.schema.ShEx import CreateFromDocument, ShapeLabel
from shexypy.shexyinterpreter.interpretations import ShapeEvaluator
from shexypy.utils.xmlutils import prettyxml


def build_argparser() -> argparse.ArgumentParser:
    """ Construct a basic argument parser.  This is a separate module so main specific parameters
    can be added separately from the parse specific arguments
    :return: argument parser
    """
    parser = argparse.ArgumentParser(description="Run ShExDoc parser")
    parser.add_argument("infile", help="Interpretation file.")
    parser.add_argument("graph", help="Name of file containing the graph")
    parser.add_argument("-f", "--format", help="Graph file format", default="turtle")
    parser.add_argument("-p", "--print", help="Print parsed XML", action="store_true")
    return parser


def parse_args(argparser: argparse.ArgumentParser, args: list) -> argparse.Namespace:
    """ Parse the input arguments
    :return: Parsed input arguments
    """
    parsed_args = argparser.parse_args(args)
    return parsed_args


def main(argv: list):
    parser_args = build_argparser()
    opts = parse_args(parser_args, argv)

    schema = CreateFromDocument(open(opts.infile).read())
    if opts.print:
        print(prettyxml(schema))
    g = Graph()
    g.parse(opts.graph, format=opts.format)
    seval = ShapeEvaluator(schema)
    ls = seval.compile(ShapeLabel("S"))
    ls.test(URIRef("http://a.example/x"), g)

if __name__ == '__main__':
    main(sys.argv[1:])
