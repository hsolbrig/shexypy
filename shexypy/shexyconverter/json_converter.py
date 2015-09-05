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

from urllib.parse import urljoin

from rdflib import URIRef, XSD

from shexypy.schema.ShEx import *
from shexypy.utils.pyxb_utils import PyxbWrapper


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
                return urljoin(self._map[ns], local, allow_fragments=False)
        elif ':' not in iri and iri in self._map:
            return self._map[iri]
        return str(URIRef(iri)) if iri is not None else ""

    def namespaces(self):
        return self._map


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
        self._exclude_prefixes = self.schema.exclude_prefixes.split(' ') + ['xml', 'xmlns']
        self.shex_schema()

    def shex_schema(self):
        """ <code>xs:Element name="Schema" type="shex:Schema</code>
        """
        self.json["prefixes"] = {prefix: url for prefix, url in self._prefixmap.namespaces().items()
                                 if prefix is not None and url and prefix not in self._exclude_prefixes}
        if self.schema.startActions:
            self.json["startAct"] = self.shex_semantic_actions(self.schema.startActions)
        if self.schema.shape:
            self.json["shapes"] = {self._uri(s.label): self.shex_shape(s) for s in self.schema.shape}
        if self.schema.valueClass:
            self.json["valueClasses"] = \
                {self.shex_iri(vc.definition.valueClassLabel if vc.definition else vc.external.ref):
                     self.shex_value_class_definition(vc) for vc in self.schema.valueClass}
        if self.schema.start:
            self.json["start"] = self._uri(self.schema.start)

    def shex_shape(self, shape: Shape) -> dict:
        """ <code>xs:complexType name="shape"</code>
        :param shape: XML Shape
        :return: S-JSON Shape Entry
        """
        rval = dict(type="shape")
        w_shape = PyxbWrapper(shape)
        self.shex_annotations_and_actions(rval, w_shape)
        [self.shex_expression_choice(rval, e) for e in w_shape.elements]
        for e in w_shape.elements:
            if e.type == "import_":
                rval.setdefault("inherit", []).append(self.shex_shape_ref(e.value.node))
            elif e.type == "extra":
                rval.setdefault(e.type, []).append(self._uri(e.value.node.ref))

        # shape.label is the dictionary key in the Schema container
        if shape.virtual:
            rval["virtual"] = shape.virtual
        if shape.closed:
            rval["closed"] = shape.closed
        return rval

    @staticmethod
    def _typed_expression(typ: str, val: dict) -> dict:
        val["type"] = typ
        return val

    def shex_expression_choice(self, target: dict, e: PyxbWrapper.PyxbElement) -> dict:
        """ <code>xs:group name="ExpressionChoice"</code>
        :param target: target type with ExpressionChoice mixin
        :param e: Wrapper for ExpressionChoice element
        :return: target
        """
        if e.type in ["someOf", "group"]:
            expr = self.shex_shape_constraint(e.value.node)
        elif e.type == "tripleConstraint":
            expr = self.shex_triple_constraint(e.value.node)
        elif e.type == "include":
            expr = dict(include=self._uri(e.value.node.ref))
        elif e.type == "wrapper":
            expr = self.shex_wrapper(e.value.node)
        else:
            expr = None
        if expr:
            target["expression"] = self._typed_expression(e.type, expr)
        return target

    def shex_wrapper(self, w: Wrapper) -> dict:
        rval = dict(type="wrapper")
        w_wrapper = PyxbWrapper(w)
        [self.shex_expression_choice(rval, e) for e in w_wrapper.elements]
        self.shex_annotations_and_actions(rval, w_wrapper)
        self.shex_cardinality(rval, w_wrapper)
        return rval

    def shex_annotations_and_actions(self, target: dict, ew: PyxbWrapper):
        """ <code>xs:group name="AnnotationsAndActions</code>
        :param target: dictionary using the group
        :param ew: xml element that contains the group
        """
        for e in ew.elements:
            if e.type == "actions":
                target["semAct"] = self.shex_semantic_actions(e.value.node)
            elif e.type == "annotation":
                target.setdefault("annotations", []).append(self.shex_annotation(e.value.node))

    def shex_shape_constraint(self, sc: ShapeConstraint) -> dict:
        """ <code>xs:complexType name="ShapeConstraint"</code>
        :param sc: A complete shape constraint
        :return: S-JSON expression
        """
        rval = dict()
        sc_wrapper = PyxbWrapper(sc)
        for e in sc_wrapper.elements:
            entry = self.shex_expression_choice({}, e)
            if "expression" in entry:
                rval.setdefault("expressions", []).append(entry["expression"])
        self.shex_annotations_and_actions(rval, sc_wrapper)
        self.shex_cardinality(rval, sc_wrapper)
        return rval


    def shex_triple_constraint(self, tc: TripleConstraint) -> dict:
        """ <code>xs:complexType name="TripleConstraint"</code>
        :param tc: TripleConstraint to process
        :return: SJson equivalent
        """
        assert not ((tc.objectConstraint or tc.object or tc.objectShape or tc.objectType) and
               (tc.subjectConstraint or tc.subject or tc.subjectShape or tc.subjectType)), \
            "Cannot mix subject and object constraints"

        tc_dict = dict(type="tripleConstraint", predicate=self.shex_iri(tc.predicate))
        if tc.valueClass:
            tc_dict["valueClassRef"] = self.shex_value_class_label(tc.valueClass)
        else:
            vc_dict = dict(type="valueClass")
            if tc.objectConstraint:
                self.shex_triple_constraint_value_class(vc_dict, tc.objectConstraint)
            if tc.object:
                vc_dict["values"] = [self.shex_iri(tc.object)]
            if tc.objectShape:
                vc_dict["reference"] = self.shex_shape_label(tc.objectShape)
            if tc.objectType:
                vc_dict["nodeKind"] = self.shex_node_type(tc.objectType)

            if tc.subjectConstraint or tc.subject or tc.subjectShape or tc.subjectType or tc.inverse:
                tc_dict["inverse"] = True
                if tc.subjectConstraint:
                    self.shex_triple_constraint_value_class(vc_dict, tc.subjectConstraint)
            if tc.subject:
                vc_dict["values"] = [self.shex_iri(tc.subject)]
            if tc.subjectShape:
                vc_dict["reference"] = self.shex_shape_label(tc.subjectShape)
            if tc.subjectType:
                vc_dict["nodeKind"] = self.shex_node_type(tc.subjectType)

            if tc.datatype:
                vc_dict["datatype"] = self._uri(tc.datatype)
            if tc.negated:
                tc_dict["negated"] = tc.negated
            tc_wrapper = PyxbWrapper(tc)
            self.shex_annotations_and_actions(tc_dict, tc_wrapper)
            self.shex_cardinality(tc_dict, tc_wrapper)
            tc_dict["value"] = vc_dict
        return tc_dict

    @staticmethod
    def shex_node_type(nt: NodeType):
        return str(nt).lower()

    def shex_annotation(self, annot: Annotation) -> list:
        """ <code>xs:complexType name="Annotation"</code>
        :param annot: Annotation
        :return: S-JSON equivalent
        """
        rval = [self._uri(annot.iri)] if annot.iri else []
        if annot.literal:
            rval.append(self.shex_rdf_literal(annot.literal))
        else:
            rval.append(self.shex_iri_ref(annot.iriref))
        return rval

    def shex_semantic_actions(self, acts: SemanticActions) -> list:
        """ <code>xs:complexType name="SemanticActions"</code>
        :param acts: actions
        :return: list of actions
        """
        return [self.shex_semantic_action(a) for a in acts.action]

    def shex_semantic_action(self, act: SemanticAction) -> dict:
        """ <code>xs:complexType name="SemanticAction"</code>
        :param act: action
        :return: S-JSON representation
        """
        # TODO: validating
        return {self._uri(act.codeDecl.iri): "%s" % self.shex_code_decl(act.codeDecl)}

    @staticmethod
    def shex_code_decl(cd: CodeDecl):
        """ <code>xs:complexType name="CodeDecl" mixed="true"</code>
        :param cd:
        :return:
        """
        return PyxbWrapper.mixed_content(cd)

    def shex_value_class_definition(self, vcd: ValueClassDefinition) -> dict:
        """ <code>xs:complexType name="ValueClassDefinition"</code>
        :param vcd:
        :return:
        """
        rval = dict(type="valueClass")
        if vcd.external:
            rval["external"] = self.shex_value_class_ref(vcd.external)
        else:
            innerdef = {}
            self.shex_inline_value_class_definition(rval, vcd.definition)
            if vcd.definition.actions:
                rval["semAct"] = self.shex_semantic_actions(vcd.definition.actions)
        return rval

    def shex_inline_value_class_definition(self, vc: dict, ivcd: InlineValueClassDefinition) -> list:
        """ <code>xs:complexType name="InlineValueClassDefinition"</code>
        :param vc: dictionary to record the actual elements
        :param ivcd:
        :return:
        """
        # valueClassLabel becomes the identity
        vcd_wrapper = PyxbWrapper(ivcd)
        for e in vcd_wrapper.elements:
            if e.type == "nodetype":
                vc["nodeKind"] = self.shex_node_type(e.value.node)
            elif e.type == "datatype":
                vc[e.type] = self._uri(e.value.node)
            elif e.type == "facet":
                self.shex_xs_facet(vc, e.value.node)
            elif e.type == "or_":
                vc["reference"] = self.shex_group_shape_constr(e.value.node)
            elif e.type == "valueSet":
                vc["values"] = self.shex_value_set(e.value.node)
            else:
                assert False, "Unknown ValueClassExpression choice entry: %s" % e.type

    def shex_group_shape_constr(self, gsc: GroupShapeConstr) -> dict:
        """ <code>xs:complexType name="GroupShapeConstr"</code>
        :param gsc:
        :return:
        """
        rval = dict(type="or", disjuncts=[self.shex_shape_ref(d) for d in gsc.disjunct])
        if gsc.stringFacet:
            [self.shex_xs_facet(rval, e) for e in gsc.stringFacet]
        return rval

    # noinspection PyTypeChecker
    def shex_triple_constraint_value_class(self, vc: dict, tcvc: TripleConstraintValueClass) -> (dict, dict):
        return self.shex_inline_value_class_definition(vc, tcvc)

    def shex_value_class_label(self, l: ValueClassLabel) -> str:
        """ <code>xs:simpleType name="ValueClassLabel"</code>
        :param l:
        :return:
        """
        return self.shex_iri(l)

    def shex_value_class_ref(self, lr: ValueClassRef) -> str:
        """ <code>xs:complexType name="ValueClassRef"</code>
        :param lr:
        :return:
        """
        return self.shex_value_class_label(lr.ref)

    def shex_shape_label(self, sl: ShapeLabel) -> str:
        """ <code>xs:simpleType name="ShapeLabel"</code>
        :param sl:
        :return:
        """
        return self.shex_iri(sl)

    def shex_shape_ref(self, sr: ShapeRef) -> str:
        """ <code>xs:complexType name="ShapeRef"</code>
        :param sr:
        :return:
        """
        return self.shex_shape_label(sr.ref)

    @staticmethod
    def shex_code_label(cl: CodeLabel) -> str:
        """ <code>xs:complexType name="CodeLabel"</code>
        :param cl:
        :return:
        """
        return cl.ref.value()

    @staticmethod
    def shex_xs_facet(target: dict, f: XSFacet):
        """ <code>xs:complexType name="XSFacet"</code>
        :param target: target dictionary (ValueClass)
        :param f: facet to transform
        """
        if f.pattern:
            target["pattern"] = f.pattern
        elif f.not_:
            target["negated"] = True
        elif f.minLength:
            target["minlength"] = f.minLength
        elif f.maxLength:
            target["maxlength"] = f.maxLength
        elif f.length:
            target["length"] = f.length
        elif f.minValue:
            if f.minValue.open:
                target["minexclusive"] = f.minValue.value()
            else:
                target["mininclusive"] = f.minValue.value()
        elif f.maxValue:
            if f.maxValue.open:
                target["maxexclusive"] = f.maxValue.value()
            else:
                target["maxinclusive"] = f.maxValue.value()
        elif f.totalDigits:
            target["totaldigits"] = f.totalDigits
        elif f.fractionDigits:
            target["fractiondigits"] = f.fractionDigits
        else:
            assert False, "Unknown facet %s" % f

    # shex_endpoint  is covered in the xs_facet logic above

    # noinspection PyTypeChecker
    @staticmethod
    def shex_string_facet(target: dict, sf: StringFacet):
        ShExSchema.shex_xs_facet(target, sf)

    # noinspection PyTypeChecker
    @staticmethod
    def shex_numeric_facet(target: dict, nf: NumericFacet):
        ShExSchema.shex_xs_facet(target, nf)

    def shex_value_set(self, vs: ValueSet) -> list:
        if vs.iriRange:
            return [self.shex_iri_range(e) for e in vs.iriRange]
        elif vs.rdfLiteral:
            return [self.shex_rdf_literal(e) for e in vs.rdfLiteral]
        elif vs.integer:
            return ['"%i"^^%s' % (e, XSD.integer) for e in vs.integer]
        elif vs.decimal:
            return ['"%d"^^%s' % (e, XSD.decimal) for e in vs.decimal]
        elif vs.double:
            return ['"%e"^^%s' % (e, XSD.double) for e in vs.double]
        elif vs.boolean:
            return ['"%s"^^%s' % (e, XSD.boolean) for e in vs.boolean]
        else:
            assert False, "Unknown ValueSet type"

    def shex_iri_stem(self, ist: IRIStem) -> dict:
        if ist.base and not ist.stem:
            return self.shex_iri(ist.base)
        else:
            return dict(stem=self.shex_iri(ist.base)) if ist.base else dict(stem=dict(type="wildcard"))

    def shex_iri_range(self, irir: IRIRange) -> object:
        """
        :param irir:
        :return:
        """
        def add_stem_type(d: dict, v: IRIStem):
            if v.stem:
                d["type"] = "stem"
            return d

        # If just a base, return the IRI
        if irir.base and not irir.stem and not irir.exclusion:
            return self.shex_iri(irir.base)
        rval = dict(type="stemRange")
        rval.update(self.shex_iri_stem(irir))
        if irir.exclusion:
            rval["exclusions"] = [add_stem_type(self.shex_iri_stem(e), e) for e in irir.exclusion]
        return rval

    def shex_rdf_literal(self, lit: RDFLiteral) -> str:
        rval = '"' + lit.value() + '"'
        if lit.datatype:
            rval += '^^' + self.shex_iri(lit.datatype)
        if lit.langtag:
            rval += '@' + lit.langtag
        return rval

    def shex_iri(self, iri: IRI) -> str:
        return self._uri(str(iri))

    def shex_iri_ref(self, ref: IRIRef) -> str:
        return self.shex_iri(ref.ref)

    def shex_prefixed_name(self, pn: PrefixedName) -> str:
        return self._uri(str(pn))

    @staticmethod
    def shex_cardinality(target: dict, card: PyxbWrapper):
        minv = card.node.min if card.node.min is not None else 1
        maxv = card.node.max if card.node.max is not None else 1
        if minv == maxv:
            if minv != 1:
                target["length"] = minv
        else:
            target["min"] = minv
            target["max"] = '*' if maxv == "unbounded" else maxv

    def _uri(self, element):
        """ Map element into a complete URI
        :param element: URI or QNAME
        :return: URI
        """
        return self._prefixmap.uri_for(PyxbWrapper.proc_unicode(element))

