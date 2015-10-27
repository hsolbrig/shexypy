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
from antlr4.error.ErrorListener import ErrorListener

from dirlistproc.DirectoryListProcessor import DirectoryListProcessor
from antlr4 import *
from antlr4.InputStream import InputStream


_curdir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(_curdir, '..'))

from shexypy.utils.xmlutils import prettyxml
from shexypy.shexyparser.parser_impl.ShExDocVisitor_impl import ShExDocVisitor_impl

START_RULE = "shExDoc"
GRAMMAR_RULE = "ShExDoc"
VISITOR = "ShExDocVisitor_impl"

failing_tests = [
    "1refbnode_with_spanning_PN_CHARS_BASE1.shex",
    "1val1STRING_LITERAL1_with_all_controls.shex",
    "refbnode_with_spanning_PN_CHARS_BASE1.shex",
    "1val1STRING_LITERAL1_with_ascii_boundaries.shex",
    "1val1STRING_LITERAL1_with_UTF8_boundaries.shex",
    "_all.shex",
    "open1dotclose.shex",
    "open1dotcloseAnnot3.shex",
    "open1dotclosecardOpt.shex",
    "open1dotcloseCode1.shex",
    "openopen1dotcloseCode1closeCode2.shex"
]


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


class ParseErrorListener(ErrorListener):

    def __init__(self):
        self.n_errors = 0

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.n_errors += 1

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        self.n_errors += 1

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        self.n_errors += 1

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        self.n_errors += 1


def do_parse(infile: InputStream) -> ShExDocVisitor_impl:
    lexer = get_lexer(infile)
    error_listener = ParseErrorListener()
    lexer.addErrorListener(error_listener)
    tokens = CommonTokenStream(lexer)
    tokens.fill()
    if error_listener.n_errors:
        return None
    parser = get_parser(tokens)
    parser.addErrorListener(error_listener)
    tree = getattr(parser, START_RULE)()
    visitor = get_object(VISITOR)()
    visitor.visit(tree)
    return visitor if not error_listener.n_errors else None


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

nskipped = 0


def file_filter(fn):
    global nskipped
    if fn in failing_tests:
        print("*** Skipping %s" % fn)
        nskipped += 1
        return False
    return True


def main(argv: list):
    global nskipped
    sys.path.append(os.path.join(_curdir, '../shexypy/shexyparser/parser'))
    sys.path.append(os.path.join(_curdir, '../shexypy/shexyparser/parser_impl'))

    dlp = DirectoryListProcessor(argv, "ShEx to XML Parser", '.shex', '.xml')
    nskipped = 0
    nfiles, npassed = dlp.run(proc_file, file_filter=file_filter)

    def _pl(s, n) -> (int, str):
        return n, s if n == 1 else (s + 's')

    print(file=sys.stderr)
    print("***** " + ("Success" if nfiles == npassed else "FAILURE") + " *****", file=sys.stderr)
    print("\t%d %s Processed" % _pl("File", nfiles), file=sys.stderr)
    print("\t%d %s" % _pl("Error", nfiles - npassed), file=sys.stderr)
    print("\t%d %s Skipped" % _pl("File", nskipped), file=sys.stderr)

if __name__ == '__main__':
    main(sys.argv[1:])
