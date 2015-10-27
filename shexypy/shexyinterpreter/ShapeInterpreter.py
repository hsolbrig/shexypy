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
from itertools import permutations, product
import re

from rdflib import Graph, URIRef, XSD, Literal

from shexypy.schema.ShEx import *
from shexypy.utils.rdfutils import Triple, RDFTerm
from shexypy.shexyinterpreter.ShapeCompiler import CompiledShape
from shexypy.utils.PrefixMap import PrefixMap
from shexypy.utils.pyxb_utils import test_numeric_facet, PyxbChoice
from shexypy.utils.xmlutils import prettyxml


class SchemaException(Exception):
    pass


class ShapeInterpreter:
    def __init__(self, schema: Schema, schema_dom, g: Graph = None):
        """ Schema interpreter
        :param schema: definition
        :param schema_dom: equivalent in dom to get the namespace map
        """
        self.schema = schema
        self._nsmap = PrefixMap(schema, schema_dom)
        self._default_namespace = schema.default_namespace if schema.default_namespace else ''
        self._shapes = {self._nsmap.uri_for(sh.label): sh for sh in schema.shape}
        self._compiled_shapes = {}
        self._triple_results = {}
        self._graph = g

    @property
    def graph(self):
        return self._graph

    @graph.setter
    def graph(self, g: Graph):
        self._graph = g
        self._triple_results = {}

    def _i_shape_subject(self, subj, cs: CompiledShape) -> bool:
        """ Evaluate the shape against the set of triples with subject subj.
        :param subj: subject to evaluate
        :param cs: compiled shape to use in interpretation
        :return: True and a list of predicate/object permutations
        """

        # Everything passes an empty shape
        if len(cs.tripleconstraints) == 0:
            return True

        # Create a list of unique permutations of all the triples in the graph with subject = subj
        #   If there are any predicates in the predicate_objects list that aren't constrained, fail if
        #   the shape is closed and ignore if it is open
        predicate_objects = [e for e in self.graph.predicate_objects(subject=subj)]
        unmatched_predicate_objects = [e for e in predicate_objects if str(e[0]) not in cs.predmap]
        if unmatched_predicate_objects and cs.closed:
            return False
        target_predicate_objects = [po for po in predicate_objects if po not in unmatched_predicate_objects]
        if len(target_predicate_objects) > 4:
            pred_obj_permutations = permutations(target_predicate_objects)
        else:
            pred_obj_permutations = list(set(permutations(target_predicate_objects)))
        # if len(pred_obj_permutations) > 100:
        #     print("   PERMUTATIONS: %d" % len(pred_obj_permutations))

        # For each permutation, create a cross product of all candidate tripleconstraints with the same
        # predicate as that in the permutation. The string equivalent of this permutation becomes the pattern
        # that we match against the complied shape match pattern.
        #
        # If the permutation matches, add it to the candidates list.  The key is the particular permutation and
        # the value is the list of all possible tripleconstraints that it will pass
        #
        # If the target predicate isn't in the predicate isn't in the predicate to tripleconstraint map, it
        # is ignored if the shape
        candidates = dict()
        for pred_obj_permutation in pred_obj_permutations:
            tc_idx_list = [cs.predmap[str(pred)] for (pred, _) in pred_obj_permutation if str(pred) in cs.predmap]
            tc_idx_cross_product = list(product(*tc_idx_list))
            for tc_idx_list in tc_idx_cross_product:
                match_str = ''.join(tc_idx_list)
                if cs.matchpattern.fullmatch(match_str):
                    candidates.setdefault(pred_obj_permutation, []).append(tc_idx_list)

        # We now have a set of candidates, the key being a particular ordering of the list of predicate/objects for
        # the supplied subject and the data being a list of the tripleconstraint(s) that the ordering would have to
        # pass for the shape to pass.

        # Determine which, if any, predicate/object orderings pass the corresponding triples in the list
        for pred_obj_permutation, tc_idx_lists in candidates.items():
            for tc_idx_list in tc_idx_lists:
                if self.i_tc_idx_entry(subj, cs, tc_idx_list, pred_obj_permutation):
                    return True
        return False

    def i_tc_idx_entry(self, subj, cs: CompiledShape, tc_idx_list: list, pred_obj_permutation: list) -> bool:
        """ Interpret the set of triple constraints in the particular predicate/object list and triple_constraint indices
        :param subj: Subject being tested
        :param cs: complied shape
        :param tc_idx_list:
        :param pred_obj_permutation:
        :return:
        """
        # TODO: Clean this up
        # hit = tc_idx_list == ('0 ', '2 ', '2 ', '3 ')
        # if hit:
        #     print("EVAL: " + ''.join(tc_idx_list))
        #     print(', '.join(["( %s, %s)" % (e[0].split('/')[-1], e[1].split('/')[-1]) for e in pred_obj_permutation]))
        hit = False
        for i in range(len(tc_idx_list)):
            idx = tc_idx_list[i]
            pred, obj = pred_obj_permutation[i][0], pred_obj_permutation[i][1]
            if int(idx) != 0 and idx.startswith('0'):
                # Extra: The permutation that matched this can't have matched any other triple.
                for tripc_num in cs.predmap[str(pred)]:
                    if int(tripc_num) == 0 or not tripc_num.startswith('0'):
                        if self.i_tripleconstraint(Triple(subj, pred, obj), cs.tripleconstraints[int(tripc_num)]):
                            return False
            else:
                rslt = self.i_tripleconstraint(Triple(subj, pred, obj),
                                               cs.tripleconstraints[int(tc_idx_list[i])])
                # if hit:
                #     print("entry: %i (%s) (%s, %s, %s) = %s" % (i, tc_idx_list[i], subj, pred, obj, rslt))
                if not rslt:
                    return False

        return True

    def i_shape(self, subj: URIRef, shape: ShapeLabel) -> bool:
        """ Interpret subject subj and shape in the graph
        :param subj: subject of interpretation
        :param shape: name of shape
        :return: success indicator
        """
        assert self.graph is not None, "Graph must be supplied"
        if str(shape) not in self._shapes:
            raise SchemaException("Unresolved shape reference: %s" % str(shape))
        if shape not in self._compiled_shapes:
            self._compiled_shapes[shape] = CompiledShape(self._nsmap, self._shapes[str(shape)], self)
        cs = self._compiled_shapes[shape]

        if subj:
            return self._i_shape_subject(subj, cs)
        else:
            for s in self.graph.subjects():
                if self._i_shape_subject(s, cs):
                    return True
        return False

    def i_tripleconstraint(self, t: Triple, c: TripleConstraint) -> bool:
        k = (t, c)
        if k in self._triple_results:
            return self._triple_results[k]
        if URIRef(self._nsmap.uri_for(c.predicate)) == t.p:
            rslt = (not c.objectConstraint or self.i_so_constraint(c.objectConstraint, t.o)) and \
                   (not c.subjectConstraint or self.i_so_constraint(c.subjectConstraint, t.s)) and \
                   (not c.object or self.i_so(c.object, t.o)) and \
                   (not c.subject or self.i_so(c.subject, t.s)) and \
                   (not c.objectShape or self.i_so_shape(c.objectShape, t.o)) and \
                   (not c.subjectShape or self.i_so_shape(c.subjectShape, t.s)) and \
                   (not c.objectType or self.i_so_type(c.objectType, t.o)) and \
                   (not c.subjectType or self.i_so_type(c.subjectType, t.s)) and \
                   (not c.datatype or self.i_datatype(c.datatype, t.o)) and \
                   (not c.valueClass or self.i_value_class(c.valueClass, t.o))
        else:
            rslt = False
        rval = rslt if c.negated is None or not c.negated else not rslt
        self._triple_results[k] = rval
        return rval

    def i_so_constraint(self, c: TripleConstraintValueClass, o: RDFTerm) -> bool:
        rslt = (not c.facet or self.i_facet(c.facet, o)) and \
               (not c.valueSet or self.i_value_set(c.valueSet, o))
        return rslt

    def i_so(self, c: IRI, o: RDFTerm) -> bool:
        return o.is_iri and str(o.iri) == str(c)

    def i_so_shape(self, c: ShapeLabel, o: RDFTerm) -> bool:
        return False if o.is_literal else self.i_shape(o.val, c)

    @staticmethod
    def i_so_type(c: NodeType, o: RDFTerm) -> bool:
        return (c == NodeType.LITERAL and o.is_literal) or (c == NodeType.IRI and o.is_iri) or \
               (c == NodeType.BNODE and o.is_bnode) or (c == NodeType.NONLITERAL and not o.is_literal)

    def i_datatype(self, c: IRI, o: RDFTerm) -> bool:
        # TODO: Flesh this out
        return o.is_literal and \
               ((str(o.literal.datatype) == self._nsmap.uri_for(c)) or
                (not(o.literal.datatype) and self._nsmap.uri_for(c) == 'xsd:string'))

    def i_value_class(self, c: ValueClassLabel, o) -> bool:
        return True

    def i_object(self, c: IRI, o: RDFTerm) -> bool:
        return isinstance(o, URIRef) and URIRef(self._nsmap.uri_for(c)) == o

    @staticmethod
    def i_facet(fct: XSFacet, o: RDFTerm) -> bool:
        for f in fct:
            if f.pattern:
                rslt = bool(re.fullmatch(f.pattern, str(o.val)))
            elif f.not_:
                rslt = bool(re.fullmatch(f.not_, str(o.val)))
            elif f.minLength:
                rslt = len(str(o.val)) <= f.minLength
            elif f.maxLength:
                rslt = len(str(o.val)) >= f.maxLength
            elif f.length:
                rslt = len(str(o.val)) == f.length
            elif f.minValue:
                v = ShapeInterpreter._coerce_numtype(o, o.literal.value)
                f = ShapeInterpreter._coerce_numtype(o, f.minValue)
                rslt = False if v is None or f is None else f < v if f.minValue.open else f <= v
            elif f.maxValue:
                v = ShapeInterpreter._coerce_numtype(o, o.literal.value)
                f = ShapeInterpreter._coerce_numtype(o, f.maxValue)
                rslt = False if v is None or f is None else f > v if f.maxValue.open else f >= v
            elif f.totalDigits:
                rslt = bool(test_numeric_facet(o.literal.value, total_digits=f.totalDigits))
            elif f.fractionDigits:
                rslt = bool(test_numeric_facet(o.literal.value, fraction_digits=f.fractionDigits))
            else:
                assert False, "Unhandled facet"
            if not rslt:
                return False
        return True

    dtlist = {XSD.integer: int, XSD.decimal: float, XSD.double: float}

    @staticmethod
    def _coerce_numtype(o: RDFTerm, v) -> str:
        if not o.is_literal or o.literal.datatype not in ShapeInterpreter.dtlist:
            return None
        return ShapeInterpreter.dtlist[o.literal.datatype](str(v))

    def i_value_set(self, vs: ValueSet, o: RDFTerm) -> bool:
        for vse in PyxbChoice(vs).elements:
            if vse.iriRange:
                rslt = self.i_iri_range(vse.iriRange, o)
            elif vse.rdfLiteral:
                rslt = self.i_rdf_literal(vse.rdfLiteral, o)
            elif vse.integer:
                rslt = self.i_integer(vse.integer, o)
            elif vse.decimal:
                rslt = self.i_decimal(vse.decimal, o)
            elif vse.double:
                rslt = self.i_double(vse.double, o)
            elif vse.boolean:
                rslt = self.i_boolean(vse.boolean, o)
            else:
                assert False, "Unknown vse type"
            if not rslt:
                return False
        return True

    def i_iri_range(self, ir: IRIRange, o: RDFTerm):
        return self.i_iri_stem(ir, o) and not any(self.i_iri_stem(ex, o) for ex in ir.exclusion)

    @staticmethod
    def i_iri_stem(ist: IRIStem, o: RDFTerm):
        return not o.is_iri or (str(ist.base) == str(o.iri) if not ist.stem else str(o.iri).startswith(ist.base))

    def i_rdf_literal(self, rdfl: RDFLiteral, o):
        if not o.is_literal:
            return False
        lit = Literal(rdfl.value(),
                      lang=rdfl.langtag,
                      datatype=URIRef(self._nsmap.uri_for(rdfl.datatype)) if rdfl.datatype else None)
        return lit == o.literal

    @staticmethod
    def i_integer(intv, o):
        if not o.is_literal:
            return False
        lit = Literal(intv, datatype=XSD.integer)
        return lit == o.literal

    @staticmethod
    def i_decimal(decv, o):
        if not o.is_literal:
            return False
        lit = Literal(decv, datatype=XSD.decimal)
        return lit == o.literal

    @staticmethod
    def i_double(doubv, o):
        if not o.is_literal:
            return False
        lit = Literal(doubv, datatype=XSD.double)
        return lit == o.literal

    @staticmethod
    def i_boolean(boolv, o):
        if not o.is_literal:
            return False
        lit = Literal(boolv, datatype=XSD.boolean)
        return lit == o.literal
