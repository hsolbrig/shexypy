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
import os
import sys

from dirlistproc.DirectoryListProcessor import DirectoryListProcessor
from antlr4 import *
from antlr4.InputStream import InputStream


_curdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(_curdir, '..'))

from shexypy.utils.xmlutils import prettyxml

START_RULE = "shExDoc"
GRAMMAR_RULE = "ShExDoc"
VISITOR = "ShExDocVisitor_impl"


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


def proc_file(infile, outfile, _):
    if infile:
        print("Parsing " + infile, file=sys.stderr)
    else:
        print("Enter ShEx to parse:")
        print()
    result = do_parse(FileStream(infile, encoding='utf8') if infile else StdInputStream())

    if result:
        pretty_result = prettyxml(result.to_dom())
        if outfile:
            open(outfile, 'w').write(pretty_result)
        else:
            print(pretty_result)
    else:
        print("Parse failure", file=sys.stderr)
        return False


def main(argv: list):
    sys.path.append(os.path.join(_curdir, '../shexypy/shexyparser/parser'))
    sys.path.append(os.path.join(_curdir, '../shexypy/shexyparser/parser_impl'))

    dlp = DirectoryListProcessor(argv, "ShEx to XML Parser", '.shex', '.xml')
    nfiles, npassed = dlp.run(proc_file)
    print(file=sys.stderr)
    print("***** " + ("Success" if nfiles == npassed else "FAILURE") + " *****", file=sys.stderr)
    print("\t%d File%s Processed" % (nfiles, '' if nfiles == 1 else 's'), file=sys.stderr)
    print("\t%d Error%s" % (nfiles - npassed, '' if nfiles - npassed == 1 else 's'), file=sys.stderr)

if __name__ == '__main__':
    main(sys.argv[1:])
