#!/usr/bin/env bash
# Note: antlr4 can be installed with brew (doc other methods)
# need antlr4.5.1
# Generate the parser_impl
# TODO: fix absolute location
antlr4 -Dlanguage=Python3 -package shexyparser.parser -o ../shexyparser/parser -no-listener -visitor ~/Development/git/shexSpec/grammar/ShExDoc.g4
