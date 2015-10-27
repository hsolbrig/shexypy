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

import unittest
from scripts import shex_eval, shex_parser


class EvalIssuesTestCase(unittest.TestCase):
    def test_simple_xml_data(self):
        # Issue:  python shex_eval.py -i ../tests/testdata/simple.shex -g ../tests/testdata/test1.ttl
        #            -f turtle -s my:UserShape -n inst:User1 fails
        shex_eval.main('-i ../tests/testdata/simple.shex -g ../tests/testdata/test1.ttl '
                       '-gf turtle -ss my:UserShape -fn inst:User1 -p'.split())

    def test_simple_shex_data(self):
        shex_parser.main("-i ../tests/testdata/simple.shex -o ../tests/testdata/simple.xml".split())
        shex_eval.main('-i ../tests/testdata/simple.xml -if xml -g ../tests/testdata/test1.ttl '
                       '-gf turtle -ss my:UserShape -fn inst:User1 -p'.split())


if __name__ == '__main__':
    unittest.main()
