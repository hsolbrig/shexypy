#!/usr/bin/env bash
# Note: antlr4 can be installed with brew (doc other methods)
# Note: need antlr4.5.1 or later to run this!
wget https://raw.githubusercontent.com/shexSpec/grammar/master/ShExDoc.g4
antlr4 -Dlanguage=Python3 -package shexyparser.parser -o ../shexypy/shexyparser/parser -no-listener -visitor ShExDoc.g4
rm ShExDoc.g4
