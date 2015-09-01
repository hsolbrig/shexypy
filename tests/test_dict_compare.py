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
from shexypy.utils.dict_compare import dict_compare


class DictCompareTestCase(unittest.TestCase):
    def test_basic(self):
        d1 = dict(a='foo')
        d2 = dict(a='foo')
        self.assertTrue(dict_compare(d1, d2)[0])
        torf, txt = dict_compare(d1, dict(a='bar'))
        self.assertFalse(torf)
        self.assertEqual("""--- dict1
+++ dict2

< dict1.a: foo
> dict2.a: bar
""", txt)

    def test_add(self):
        d1 = dict(a='foo', b=1, c=[1, 2, 3])
        self.assertEqual("""--- a and b
+++ empty

+  a and b.a: foo
+  a and b.b: 1
+  a and b.c: [1, 2, 3]
""", dict_compare(d1, dict(), "a and b", "empty")[1])

    def test_depth(self):
        d1 = dict(a=dict(b=dict(c="c1", d="d1")))
        self.assertEqual("""--- deep1
+++ deep2

+  deep1.a.b.d: d1
""", dict_compare(d1, dict(a=dict(b=dict(c="c1"))), "deep1", "deep2")[1])

    def test_filtr(self):
        d1 = dict(a='foo', b=dict(c=1, d=2), f=dict(c=1, d=17), d=111)
        d2 = dict(a='bar', b=dict(c=0, d=3), f=dict(c=1, d=17), d=43)

        def filtr(kv1, kv2) -> bool:
            return (kv1 and kv1[0].split('.')[-1] == 'd') or (kv2 and kv2[0].split('.')[-1] == 'd')

        self.assertEqual("""--- dict1
+++ dict2

< dict1.a: foo
> dict2.a: bar
< dict1.b.c: 1
> dict2.b.c: 0
""", dict_compare(d1, d2, filtr=filtr)[1])

if __name__ == '__main__':
    unittest.main()
