# -*- coding: utf-8 -*-
# Copyright (c) 2015, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
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
import argparse
import os
import sys
from shexyparser.utils.xmlutils import prettyxml
from realshexy.interpretations import ShapeEvaluator
from shexyparser.schema.ShEx import ShapeLabel

from antlr4 import *
from antlr4.InputStream import InputStream

_curdir = os.path.abspath(os.path.dirname(__file__))


# If the lexer start rule is 'tokens' this is strictly a lexer test.  THere is no associated parser
LEXER_START_RULE_NAME = 'tokens'
START_RULE = "shExDoc"
GRAMMAR_RULE = "ShExDoc"
VISITOR = "ShExDocVisitor_impl"


def build_argparser() -> argparse.ArgumentParser:
    """ Construct a basic argument parser.  This is a separate module so main specific parameters
    can be added separately from the parse specific arguments
    :return: argument parser
    """
    parser = argparse.ArgumentParser(description="Run ShExDoc parser")
    return parser


def parse_args(argparser: argparse.ArgumentParser, args: list) -> argparse.Namespace:
    """ Parse the input arguments
    :return: Parsed input arguments
    """
    parsed_args = argparser.parse_args(args)
    return parsed_args


class StdInputStream(InputStream):
    """ Create an inputstream out of stdin
    """
    def __init__(self):
        InputStream.__init__(self, sys.stdin.read())


def get_object(name):
    """ Return an object named "name" from a package of the same name
    :param name: package/object to retrieve
    :return: reference to the actual object
    """
    module = __import__(name, fromlist=[name])
    return getattr(module, name)


def get_lexer(instream: InputStream) -> Lexer:
    """ Build a lexer for the input stream
    :param instream: input stream
    :return:
    """
    return get_object(GRAMMAR_RULE + 'Lexer')(instream)


def get_parser(tokens: CommonTokenStream) -> Parser:
    """ Build a parser
    :param tokens: token stream
    :return:
    """
    return get_object(GRAMMAR_RULE + 'Parser')(tokens)


def do_parse(infile: InputStream):
    tokens = CommonTokenStream(get_lexer(infile))
    tokens.fill()
    parser = get_parser(tokens)
    tree = getattr(parser, START_RULE)()
    visitor = get_object(VISITOR)()
    visitor.visit(tree)
    return visitor


def main(argv: list):
    sys.path.append(os.path.join(_curdir, '..'))
    sys.path.append(os.path.join(_curdir, '../shexyparser/parser'))
    sys.path.append(os.path.join(_curdir, '../shexyparser/parser_impl'))

    parser_args = build_argparser()
    parser_args.add_argument("infile", help="Input file to parse. If absent, parse stdin", nargs='?')
    parser_args.add_argument("-o", "--output", help="Destination file. If absent, stdout")
    parser_args.add_argument("-e", "--evaluate", help="Construct evaluator", action="store_true")

    opts = parse_args(parser_args, argv)

    result = do_parse(FileStream(opts.infile) if opts.infile else StdInputStream())
    if result:
        if opts.output:
            open(opts.output, 'w').write(prettyxml(result.to_dom()))
        if opts.evaluate:
            seval = ShapeEvaluator(result.schema)
            seval.compile(ShapeLabel("<S>"))
        else:
            print(prettyxml(result.to_dom()))
    else:
        print("Parse failure", file=sys.stderr)

if __name__ == '__main__':
    main(sys.argv[1:])
