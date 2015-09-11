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
from pyxb import SimpleFacetValueError
from shexypy.utils.pyxb_utils import test_numeric_facet


class FacetsTestCase(unittest.TestCase):
    def test_total_digits(self):
        self.assertIsNone(test_numeric_facet('0.001', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(0.001, test_numeric_facet('0.001', total_digits=5))
        self.assertIsNone(test_numeric_facet('100000', total_digits=5))
        self.assertAlmostEqual(100000, test_numeric_facet('100000', fraction_digits=2))
        self.assertAlmostEqual(1, test_numeric_facet('1', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(1.2, test_numeric_facet('1.2', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(1.23, test_numeric_facet('1.23', total_digits=5, fraction_digits=2))
        self.assertIsNone(test_numeric_facet('1.234', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(12, test_numeric_facet('12', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(12.3, test_numeric_facet('12.3', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(12.34, test_numeric_facet('12.34', total_digits=5, fraction_digits=2))
        self.assertIsNone(test_numeric_facet('12.345', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(-1, test_numeric_facet('-1', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(-1.2, test_numeric_facet('-1.2', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(-1.23, test_numeric_facet('-1.23', total_digits=5, fraction_digits=2))
        self.assertIsNone(test_numeric_facet('-1.234', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(-12, test_numeric_facet('-12', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(-12.3, test_numeric_facet('-12.3', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(-12.34, test_numeric_facet('-12.34', total_digits=5, fraction_digits=2))
        self.assertIsNone(test_numeric_facet('-12.345', total_digits=5, fraction_digits=2))
        
    def test_fraction_digits(self):
        self.assertAlmostEqual(1, test_numeric_facet('1', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(1.2, test_numeric_facet('1.2', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(1.23, test_numeric_facet('1.23', total_digits=5, fraction_digits=2))
        self.assertRaises(1.234, test_numeric_facet('1.234', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(12, test_numeric_facet('12', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(12.3, test_numeric_facet('12.3', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(12.34, test_numeric_facet('12.34', total_digits=5, fraction_digits=2))
        self.assertRaises(12.345, test_numeric_facet('12.345', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(-1, test_numeric_facet('-1', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(-1.2, test_numeric_facet('-1.2', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(-1.23, test_numeric_facet('-1.23', total_digits=5, fraction_digits=2))
        self.assertRaises(-1.234, test_numeric_facet('-1.234', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(-12, test_numeric_facet('-12', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(-12.3, test_numeric_facet('-12.3', total_digits=5, fraction_digits=2))
        self.assertAlmostEqual(-12.34, test_numeric_facet('-12.34', total_digits=5, fraction_digits=2))
        self.assertRaises(-12.345, test_numeric_facet('-12.345', total_digits=5, fraction_digits=2))


if __name__ == '__main__':
    unittest.main()
