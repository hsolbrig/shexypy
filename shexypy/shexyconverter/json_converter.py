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
import re
from collections import Iterable
from urllib.parse import urljoin

from rdflib import URIRef, XSD

from shexypy.schema.ShEx import *
from shexypy.utils.pyxb_utils import PyxbWrapper

# TODO: resolve the thing below -- I believe that GetNodeContext in pyxb.namespaces.resolution.py is what we need


class PrefixMap:

    """ Prefix to URI mapping.  This performs both PNAME_NS / PNAME_LN and ATPNAME_NS / ATPNAME_LN mapping.
    """
    def __init__(self, dom_schema, schema: Schema):
        """ Create a prefix to URI mapping.  We take advantage of the rdflib tools to manage this
        :param dom_schema: DOM representation of the Schema document
        :param schema: ShEx Schema instance to derive mapping from
        """
        self._nsc = pyxb.namespace.NamespaceContext.GetNodeContext(dom_schema.documentElement)
        self._map = {prefix: str(url) for prefix, url in self._nsc.inScopeNamespaces().items()}
        if schema.default_namespace:
            self._map[''] = schema.default_namespace

    def uri_for(self, iri: str) -> str:
        """ Return the URI form of the supplied IRI.  We use the presence of "://" in the incoming string to deterime
        whether it is in QName or IRI format
        :param iri: IRI to be mapped
        :return: mapped IRI
        """
        if iri and ':' in iri and '://' not in iri:
            ns, local = iri.split(':', 1)
            if ':' not in local and ns in self._map:
                return urljoin(self._map[ns], local)
        elif ':' not in iri and iri in self._map:
            return self._map[iri]
        return str(URIRef(iri)) if iri is not None else ""

    def namespaces(self):
        return self._map


unicode_re = re.compile(r'\\u([a-fA-F0-9]{4})|\\U([a-fA-F0-9]{8})')


class ShExSchema:

    """ ShEx XML Schema to JSON wrapper
    """
    def __init__(self, dom_schema):
        """ Constructor - convert the supplied schema to json
        :param dom_schema: DOM document to convert
        """
        self.schema = CreateFromDOM(dom_schema)
        self.json = dict(type="schema")

        self._prefixmap = PrefixMap(dom_schema, self.schema)
        # TODO: look up the namespaces below rather than just using the prefixes
        _exclude_prefixes = self.schema.exclude_prefixes.split(' ') + \
                            ['xmlns', 'xml', 'xsi', 'rdf', 'rdfs', 'xml1', 'default1']
        self.json["prefixes"] = {prefix: url for prefix, url in self._prefixmap.namespaces().items()
                                 if prefix is not None and url and prefix not in _exclude_prefixes}

        if self.schema.startActions:
            self.json["startAct"] = self.semantic_action(self.schema.startActions)

        if self.schema.start:
            self.json["start"] = self._uri(self.schema.start)

        if self.schema.shape:
            self.json["shapes"] = {self._prefixmap.uri_for(s.label): self.eval_shape(s) for s in self.schema.shape}

        # TODO: value class is nested in XML -- fix it
        if self.schema.valueClass:
            self.json["valueClasses"] = {self._uri(self.valueClass.valueClassLabel): self.schema_value_class(vc.valueClass)
                                         for vc in self.schema.valueClass}

    def schema_value_class(self, vc):
        vcd = dict(type="valueClass")
        self.value_class(vcd, vc)
        return vcd

    def eval_shape(self, shape: Shape) -> dict:
        """ Process an XML Shape Element
        :param shape: XML Shape
        :return: Corresponding S-Json dictionary
        """
        rval = dict(type="shape")
        if shape.virtual:
            rval["virtual"] = shape.virtual
        if shape.closed:
            rval["closed"] = shape.closed
        w_shape = PyxbWrapper(shape)
        expressions = []
        for e in w_shape.elements:
            if e.type == "extra":
                rval.setdefault(e.type, []).append(self._uri(e.value.node.ref))
            elif e.type == "include":
                rval.setdefault("inherit", []).append(self._uri(e.value.node.ref))
            elif e.type == "actions":
                rval["semAct"] = self.semantic_action(e.value.node)
            elif e.type == "annotation":
                rval.setdefault(e.type, []).extend(self.annotations(e.value.node))
            else:
                expressions.append(self.expression_group(e))
        if len(expressions) > 1:
            rval["expression"] = dict(type="group")
            rval["expression"]["type"] = "group"
            rval["expression"]["expressions"] = expressions
        elif len(expressions):
            rval["expression"] = expressions[0]
        return rval

    def expression_group(self, e: PyxbWrapper.PyxbElement) -> dict:
        """ Process the expression group represented by e
        :param e: Wrapper for expressionGroup choice
        :return:
        """
        if e.type == "someOf":
            return dict(type=e.type, expressions=[self.expression_group(s) for s in e.value.elements])
        elif e.type == "group":
            return dict(type=e.type, expressions=[self.expression_group(s) for s in e.value.elements])
        elif e.type == "tripleConstraint":
            return self.triple_constraint(e.value.node)
        elif e.type == "include":
            return dict(type=e.type, include=self._uri(e.value.node.ref))
        elif e.type == "wrapper":
            return self.wrapper(e.value.node)
        else:
            assert False, "Unknown type %s" % e.type

    def triple_constraint(self, tc: TripleConstraint):
        """ Process a triple constraint
        :param tc: TripleConstraint to process
        :return: SJson equivalent
        """
        assert not ((tc.objectConstraint or tc.object or tc.objectShape or tc.objectType) and
               (tc.subjectConstraint or tc.subject or tc.subjectShape or tc.subjectType)), \
            "Cannot mix subject and object constraints"

        tc_dict = dict(type="tripleConstraint", predicate=self._uri(tc.predicate))
        vc_dict = dict(type="valueClass")
        self.cardinality(tc, tc_dict)
        if tc.objectConstraint:
            self.value_class(vc_dict, tc.objectConstraint)
        if tc.object:
            vc_dict["values"] = [self._uri(tc.object)]
        if tc.objectShape:
            vc_dict["reference"] = self._uri(tc.objectShape)
        if tc.objectType:
            vc_dict["nodeKind"] = tc.objectType.lower()

        if tc.subjectConstraint or tc.subject or tc.subjectShape or tc.subjectType or tc.inverse:
            tc_dict["inverse"] = True
            if tc.subjectConstraint:
                self.value_class(vc_dict, tc.subjectConstraint)
            if tc.subject:
                vc_dict["values"] = [self._uri(tc.subject)]
            if tc.subjectShape:
                vc_dict["reference"] = self._uri(tc.subjectShape)
            if tc.subjectType:
                vc_dict["nodeKind"] = tc.subjectType.lower()

        if tc.datatype:
            vc_dict["datatype"] = tc.datatype
        if tc.negated:
            tc_dict["negated"] = tc.negated
        if tc.annotation:
            tc_dict["annotations"] = self.annotations(tc.annotation)
        if tc.actions:
            tc_dict["semAct"] = self.semantic_action(tc.actions)
        tc_dict["value"] = vc_dict
        return tc_dict

    def wrapper(self, wrap: PyxbWrapper.PyxbElement):
        wrapd = dict(type="wrapper")
        # TODO: figure out how to get the inner expression installed correctly
        self.cardinality(wrap.value.node, wrapd)

        for e in wrap.value.node.wrapper.elements:
            if e.type == 'annotation':
                wrapd["annotations"] = self.annotations(e.value.node.annotation)
            if e.type == "actions":
                wrapd["semAct"] = self.semantic_action(e.value.node.actions)
        return wrapd


    def value_class(self, vcd: dict, vc: ValueClass):
        """ Process a value class
        :param vcd: value class dictionary
        :param vc: value class object
        """
        for facet in vc.facet:
            self.facet(vcd, facet)
        if vc.or_:
            for or_entry in vc.or_:
                disjuncts = [self._uri(e.ref) for e in or_entry.disjunct]
                vcd["reference"] = dict(type="or")
                vcd["reference"]["disjuncts"] = disjuncts
        if vc.valueSet:
            vcd["values"] = [self.value_set(e) for e in PyxbWrapper(vc.valueSet[0]).elements]
        # TODO: Have some sort of problem here - single ref, multiple labels
        if vc.valueClassLabel:
            vcd["valueClassRef"] = self._uri(vc.valueClassLabel[0].ref)

    def value_set(self, entry: PyxbWrapper.PyxbElement) -> object:
        node = entry.value.node
        if entry.type == 'iriRange':
            if not node.exclusion and not node.stem:
                return self._uri(node.base)
            else:
                stem_uri = self._uri(node.base)
                rval = dict(type="stemRange", stem=stem_uri if stem_uri else dict(type="wildcard"))
                exclusions = [self.stem_or_iri(n) for n in node.exclusion]
                if exclusions:
                    rval["exclusions"] = exclusions
                return rval
        elif entry.type == 'rdfLiteral':
            if node.datatype:
                suffix = "^^%s" % self._uri(node.datatype)
            elif node.langtag:
                suffix = "@%s" % node.langtag
            else:
                suffix = ''
            return '"%s"' % node.value() + suffix
        elif entry.type == 'integer':
            return '"%i"^^%s' % (node, XSD.integer)
        elif entry.type == 'decimal':
            return '"%d"^^%s' % (node, XSD.decimal)
        elif entry.type == 'double':
            return '"%e"^^%s' % (node, XSD.double)
        elif entry.type == 'boolean':
            return '"%s"^^%s' % (node, XSD.boolean)
        else:
            assert False, "Unknown ValueSet type: " + entry.type

    def annotations(self, annots):
        """ Create a list of annotations.
        :param annots: annotation node(s)
        :return: list of S-Json annotation references
        """
        rval = []
        for a in (annots if isinstance(annots, Iterable) else [annots]):
            annot = [self._uri(a.iri)] if a.iri else []
            if a.literal:
                annot.append(self.rdf_literal(a.literal))
            else:
                annot.append(self._uri(a.iriref))
            rval.append(annot)
        return rval

    def semantic_action(self, actions):
        """ Return a list of semantic actions
        :param actions: set of actions to be listified
        :return: list of S-Json representations
        """
        return [{self._uri(cd.codeDecl.iri): "%s" % self._mixed_content(cd.codeDecl)} for cd in actions.action]

    @staticmethod
    def facet(vc: dict, f: XSFacet):
        """ Process a facet and transform the result into the dictionary
        :param vc: target dictionary (ValueClass)
        :param f: facet to transform
        """
        if f.pattern:
            vc["pattern"] = f.pattern
        elif f.not_:
            vc["negated"] = True
        elif f.minLength:
            vc["minlength"] = f.minLength
        elif f.maxLength:
            vc["maxlength"] = f.maxLength
        elif f.length:
            vc["length"] = f.length
        elif f.minValue:
            if f.minValue.open:
                vc["minexclusive"] = f.minValue.value()
            else:
                vc["mininclusive"] = f.minValue.value()
        elif f.maxValue:
            if f.maxValue.open:
                vc["maxexclusive"] = f.maxValue.value()
            else:
                vc["maxinclusive"] = f.maxValue.value()
        elif f.totalDigits:
            vc["totaldigits"] = f.totalDigits
        elif f.fractionDigits:
            vc["fractiondigits"] = f.fractionDigits
        else:
            assert False, "Unknown facet %s" % f

    @staticmethod
    def cardinality(card, target):
        minv = card.min if card.min is not None else 1
        maxv = card.max if card.max is not None else 1
        if minv == maxv:
            if minv != 1:
                target["length"] = minv
        else:
            target["min"] = minv
            target["max"] = '*' if maxv == "unbounded" else maxv

    def rdf_literal(self, lit):
        rval = '"' + lit.value() + '"'
        if lit.datatype:
            rval += '^^' + self._uri(lit.datatype)
        if lit.langtag:
            rval += '@' + lit.langtag
        return rval

    def _uri(self, element):
        return self._prefixmap.uri_for(self.proc_unicode(element))

    @staticmethod
    def proc_unicode(txt):
        def map_unicode(hex_str) -> str:
            char_code = int(hex_str, 16)
            if char_code < 0xFFFF:
                return chr(char_code)
            else:
                char_code -= 0x10000
                return chr(0xD800 + (char_code >> 10)) + chr(0xDC00 + (char_code & 0x3FF))

        def unescape(t):
            """ Unescape the CODE escape characters in txt
            :param t: string to be unescaped
            :return: unescaped equivalent
            """
            return re.sub(r'\\\\', r'\\', re.sub(r'\\%', '%', t)) if t else ""

        rval = ''
        pos = 0
        utxt = unescape(txt)
        for e in unicode_re.finditer(utxt):
            rval += utxt[pos:e.start()] + map_unicode(e.group(1))
            pos = e.end()
        return rval + utxt[pos:]

    @staticmethod
    def _mixed_content(item):
        return ''.join([ShExSchema.proc_unicode(e.value) if isinstance(e, pyxb.binding.basis.NonElementContent)
                        else "toDOM(e)" for e in item.orderedContent()])

    def stem_or_iri(self, node):
        if node.stem:
            stem_uri = self._uri(node.base)
            return dict(type="stem", stem=stem_uri if stem_uri else dict(type="wildcard"))
        else:
            return self._uri(node.base)
