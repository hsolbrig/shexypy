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
from shexyparser.schema.ShEx import *
from shexyparser.utils.xmlutils import prettyxml
from pyxb.utils import domutils


class SchemaTestCase(unittest.TestCase):
    def test_simple_xml(self):
        schema = Schema()
        shape = Shape()
        shape.label = "http://a.example/IssueShape"
        irirange = IRIRange()
        irirange.base = "rdf:type"
        vs = ValueSet()
        vs.iriRange.append(irirange)
        oc = ValueClass()
        oc.valueSet = vs
        tc = TripleConstraint()
        tc.predicate = "rdf:type"
        tc.objectConstraint = oc
        shape.tripleConstraint.append(tc)
        schema.shape.append(shape)
        print()
        print(prettyxml(schema))

    @staticmethod
    def _schema():
        schema = Schema()
        shape = Shape()
        shape.label = "http://a.example/IssueShape"
        schema.shape.append(shape)
        Namespace.setPrefix(prefix="shex")
        return schema, shape

    def test_namespace(self):
        schema, _ = self._schema()
        rdf = pyxb.namespace.NamespaceForURI("http://www.w3.org/1999/02/22-rdf-syntax-ns#", create_if_missing=True)
        schema_dom = schema.toDOM()
        domutils.BindingDOMSupport().addXMLNSDeclaration(schema_dom.documentElement, rdf, "rdf")
        print()
        print(prettyxml(schema_dom))

    def test_cardinality(self):
        schema, shape = self._schema()
        tc = TripleConstraint()
        tc.min = 2
        tc.max = "unbounded"
        tc.predicate = "http://foo.bar"
        shape.tripleConstraint.append(tc)
        print()
        print(prettyxml(schema))

    def test_annotation(self):
        schema, shape = self._schema()
        tc = TripleConstraint()
        ann = Annotation()
        ann.iri = "http://ann.com"
        ann.iriref = "http://ann.com/2"
        tc.annotation.append(ann)
        ann = Annotation()
        ann.iri = "http://ann.com/2"
        lit = RDFLiteral("abc")
        ann.literal = lit
        tc.annotation.append(ann)
        shape.tripleConstraint.append(tc)
        print()
        print(prettyxml(schema))

    def test_attributes(self):
        schema, shape = self._schema()
        tc = TripleConstraint()
        tc.min = 0
        tc.max = 2
        tc.predicate = "http://foo.bar"
        tc.object = "ex:object"
        tc.objectShape = "foo"
        tc.subject = "ex.subject"
        tc.subjectShape = "bar"
        tc.negated = True
        tc.datatype = "xs:string"
        tc.objectType = NodeType.LITERAL
        tc.subjectType = NodeType.IRI
        shape.tripleConstraint.append(tc)
        print()
        print(prettyxml(schema))

if __name__ == '__main__':
    unittest.main()
