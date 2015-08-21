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
import rdflib
import argparse



def build_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run shexspec test suite (http://shexspec.github.io/test-suite)")
    parser.add_argument("manifest", help="Manifest file location")
    return parser


def parse_args(argparser: argparse.ArgumentParser, args: list) -> argparse.Namespace:
    """ Parse the input arguments
    :return: Parsed input arguments
    """
    parsed_args = argparser.parse_args(args)
    parsed_args.lexerOnly = False
    parsed_args.grammar_title = parsed_args.grammar[0].upper() + parsed_args.grammar[1:]
    return parsed_args

def eval_manifest(opts: argparse.Namespace, manifest: rdflib.Graph):
    for m in manifest.subjects()

def main(argv: list):
    parser_args = build_argparser()
    opts = parse_args(parser_args, argv)
    manifest_g = rdflib.Graph()
    manifest = g.parse(opts.manifest)

    result = do_test(opts, FileStream(opts.infile) if opts.infile else StdInputStream())
    if result:
        print(result)

if __name__ == '__main__':
    main(sys.argv[1:])