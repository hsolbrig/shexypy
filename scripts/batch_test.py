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
import os


from antlr4 import FileStream


def main(argv: list):
    _curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
    sys.path.append(os.path.join(_curdir, '../../ECLparser/parser'))
    sys.path.append(os.path.join(_curdir, '../../ECLparser/parser_impl'))
    sys.path.append(os.path.join(_curdir, '../..'))
    from ECLparser.scripts.TestRig_mod import build_argparser, parse_args, do_parse

    parser_args = build_argparser()
    parser_args.add_argument("-i", "--interp", help="Interpret output", action="store_true")
    parser_args.add_argument("-d", "--dir", help="Test directory", default='.')
    parser_args.add_argument("-f", "--file", help="File pattern to match")
    parser_args.add_argument("-o", "--outdir", help="Output directory for recording expected results")
    parser_args.add_argument("-s", "--sql", help="Output SQL", action="store_true")
    opts = parse_args(parser_args, argv)
    nviewed = nfailed = nsuccess = nexceptions = 0
    for (dirpath, _, filenames) in os.walk(opts.dir):
        for fn in filenames:
            if not fn.startswith('.') and not fn.endswith('.output') and (not opts.file or fn.startswith(opts.file)):
                print("PARSING: " + fn)
                result = do_parse(opts, FileStream(os.path.join(dirpath, fn)))
                nviewed += 1
                if not result:
                    print("FAILED")
                    nfailed += 1
                elif opts.interp:
                    # try:
                        print_results(opts, dirpath, fn, i_expressionConstraint(ss, result))
                        print("SUCCESS")
                        nsuccess += 1
                    # except Exception as e:
                    #     print_results(opts, dirpath, fn, None, e)
                    #     print("EXCEPTION")
                    #     nexceptions += 1
    print("Parsed %s files:" % nviewed)
    print("\tSuccess: %s" % nsuccess)
    print("\tParse Failure: %s" % nfailed)
    print("\tEvaluation Failure: %s" % nexceptions)


if __name__ == '__main__':
    main(sys.argv[1:])
