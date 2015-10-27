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
import os

from rdflib import Literal

from shexypy.utils.manifest import *

ex = Namespace('http://example.org/')


class ManifestTestCase(unittest.TestCase):
    def test_manifest(self):
        mfst = ShExManifest(os.path.abspath(os.path.join('testdata', 'manifest.ttl')), 'n3')
        self.assertEqual(set(mfst.entries.keys()),
                         {'a-string-syntax', 'simple-star', 'a-string-valid', 'conjunction1', 'a-string-no-valid',
                          'conjunction1', 'conjunction2', 'conjunction3', 'conjunction4', 'disjunction1',
                          'disjunction2', 'disjunction3', 'disjunction4', 'star0', 'star1', 'star2', 'star3',
                          'plus0no', 'plus1', 'plus2', 'plus3', 'country-observations-valid', 'user1', 'user2',
                          'nonIRI1', 'nonIRI2', 'iri1', 'bNode', 'nonLiteral1', 'nonIRI2', 'nonBNode1',
                          'nonBNode2', 'nonBNode3', 'ab-ab', 'ab-a', 'xsd_double_simplified', 'regex_aa'})

    def test_attributes(self):
        mfst = ShExManifest(os.path.abspath(os.path.join('testdata', 'manifest.ttl')), 'n3')
        me = mfst.entries['a-string-valid']
        self.assertEqual(1, len(me))
        me = me[0]
        self.assertEqual(me.comments, 'label a with property p and a string')
        self.assertEqual(me.status, mf.proposed)
        self.assertEqual(me.subject_iri, ex.x)
        self.assertEqual(me.start_shape, ex.a)
        self.assertTrue(me.should_parse)
        self.assertTrue(me.should_pass)

        me = mfst.entries['disjunction4']
        self.assertEqual(1, len(me))
        me = me[0]
        self.assertTrue(me.should_parse)
        self.assertFalse(me.should_pass)

        me = mfst.entries['simple-star']
        self.assertEqual(1, len(me))
        me = me[0]
        self.assertTrue(me.should_parse)
        self.assertFalse(me.should_pass)

    def test_shex(self):
        mfst = ShExManifest(os.path.abspath(os.path.join('testdata', 'manifest.ttl')), 'n3')
        schema = open(os.path.join('testdata', 'country-observations.shex')).read()
        self.assertEqual(schema, mfst.entries['country-observations-valid'][0].schema)

    def test_instances(self):
        mfst = ShExManifest(os.path.abspath(os.path.join('testdata', 'manifest.ttl')), 'n3')
        self.assertEqual(
            {(URIRef('http://example.org/c1'), URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type'),
              URIRef('http://example.org/Country')), (URIRef('http://example.org/c1'),
              URIRef('http://example.org/observation'), URIRef('http://example.org/o1')),
             (URIRef('http://example.org/c1'), URIRef('http://example.org/observation'),
              URIRef('http://example.org/o2')),
             (URIRef('http://example.org/o2'), URIRef('http://example.org/value'),
              Literal('34', datatype=URIRef('http://www.w3.org/2001/XMLSchema#integer'))),
             (URIRef('http://example.org/c1'), URIRef('http://www.w3.org/2000/01/rdf-schema#label'), Literal('Spain')),
             (URIRef('http://example.org/o1'), URIRef('http://example.org/value'),
              Literal('23', datatype=URIRef('http://www.w3.org/2001/XMLSchema#integer')))},
            set(mfst.entries['country-observations-valid'][0].instance().triples((None, None, None))))


if __name__ == '__main__':
    unittest.main()
