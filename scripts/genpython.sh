#!/usr/bin/env bash

# Generate the parser_impl
antlr4 -Dlanguage=Python3 -package shexyparser.parser -o ../shexyparser/parser -no-listener -visitor ~/Development/git/shexSpec/grammar/ShExDoc.g4
# sed -e "s/from ShExDocVisitor import/from shexyparser.parser.ShExDocVisitor import/" -i "" ../shexyparser/parser/ShExDocParser.py
