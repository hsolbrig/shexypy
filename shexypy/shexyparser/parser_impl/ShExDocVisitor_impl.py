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
from xml.sax.saxutils import escape
from urllib.parse import urljoin

from collections import Iterable

from rdflib import RDF, BNode
from pyxb.xmlschema.structures import datatypes
from pyxb.utils import domutils
from pyxb.namespace import XMLSchema_instance as Xsi, NamespaceContext
from pyxb.namespace import XMLNamespaces as Xmlns


from shexypy.shexyparser.parser.ShExDocVisitor import ShExDocVisitor
from shexypy.shexyparser.parser.ShExDocParser import ShExDocParser

from shexypy.schema.ShEx import *
exclude_namespaces = ['xsi', 'shex']


class ShExDocVisitor_impl(ShExDocVisitor):
    def __init__(self):
        ShExDocVisitor.__init__(self)
        self._schema = None             # Schema being built (type: Schema
        self.base = ""                  # Base is context specific and can be changed throughout
        self.cur_shape = None           # current working shape definition (type: Shape)
        self.shape_stack = []           # parent shape definitions
        self.cur_tc = None              # current working triple constraint definition
        self.namespaces = {}            # localn name to namespace dictionary
        dns = pyxb.namespace.CreateAbsentNamespace()    # default namespace
        self.nsc = pyxb.namespace.NamespaceContext(target_namespace=dns)
        Namespace.setPrefix(prefix="shex")
        pyxb.defaultNamespace = Namespace

    def to_dom(self):
        """ Convert into DOM and map the various namespaces
        :return:
        """
        domutils.BindingDOMSupport.SetDefaultNamespace(Namespace)
        exclusions = [ns for ns in exclude_namespaces if ns not in self.namespaces]
        if exclusions:
            self._schema.exclude_prefixes = ' '.join(exclusions)

        schema_dom = self._schema.toDOM()
        bs = domutils.BindingDOMSupport()
        for ns, url in self.namespaces.items():
            if ns:
                bs.addXMLNSDeclaration(schema_dom.documentElement,
                                       pyxb.namespace.NamespaceForURI(url, create_if_missing=True),
                                       ns)
        schema_dom.documentElement.setAttributeNS(Namespace.uri(),
                                    'xsi:schemaLocation',
                                    'http://www.w3.org/shex/ ../xsd/ShEx.xsd')
        schema_dom.documentElement.setAttributeNS(Xmlns.uri, 'xmlns:xsi', Xsi.uri())
        return schema_dom

    @property
    def schema(self):
        return self._schema

    def visitShExDoc(self, ctx: ShExDocParser.ShExDocContext) -> Schema:
        # shExDoc : directive* ((notStartAction | startActions) statement*)? EOF;  // leading CODE
        self._schema = Schema()
        self.visitChildren(ctx)

    def visitStatement(self, ctx: ShExDocParser.StatementContext):
        return self.visitChildren(ctx)

    def visitNotStartAction(self, ctx: ShExDocParser.NotStartActionContext):
        # notStartAction : start | shape | valueClassDefinition ;
        self.visitChildren(ctx)

    def visitDirective(self, ctx: ShExDocParser.DirectiveContext):
        # directive : baseDecl | prefixDecl ;
        self.visitChildren(ctx)

    def visitValueClassDefinition(self, ctx: ShExDocParser.ValueClassDefinitionContext):
        # valueClassDefinition : valueClassLabel ('=' valueClassExpr semanticActions | KW_EXTERNAL) ;
        vcd = ValueClassDefinition()
        if ctx.KW_EXTERNAL():
            vcd.external = self.visit(ctx.valueClassLabel())
        else:
            vcd.definition = self.visit(ctx.valueClassExpr())
            vcd.definition.valueClassLabel = self.visit(ctx.valueClassLabel())
            acts = self.visit(ctx.semanticActions())
            if acts:
                vcd.actions = acts
        self._schema.valueClass.append(vcd)

    def visitValueClassExpr(self, ctx: ShExDocParser.ValueClassExprContext) -> InlineValueClassDefinition:
        # valueClassExpr  : valueClass ('+' valueClass)*
        # Note that there is no visitValueClass -- just the sublabels:
        #       visitValueClassLiteral
        #       visitValueClassDatatype
        #       visitValueClassGroup
        #       visitValueClassValueSet
        #       visitValueClassAny
        assert self.cur_tc is None, "Recursion not allowed on value class definitions"
        ivcd = InlineValueClassDefinition()
        for c in ctx.valueClass():
            # We fill this out as if it were a triple constraint and then fold it back to a value class
            # Note that predicate, inverse, actions and annotations are noe included in a value class definition
            self.cur_tc = TripleConstraint()
            self.cur_tc.reversed = False
            self.visit(c)
            if self.cur_tc.objectConstraint:
                oc = self.cur_tc.objectConstraint
                ivcd.facet = oc.facet
                ivcd.or_ = oc.or_
                ivcd.valueSet = oc.valueSet
            if self.cur_tc.object:
                vs = ValueSet()
                irir = IRIRange(base=self.cur_tc.object)
                vs.iriRange = irir
                ivcd.valueSet.append(vs)
            if self.cur_tc.objectShape:
                gsc = GroupShapeConstr()
                sr = ShapeRef(ref=self.cur_tc.objectShape)
                gsc.disjunct.append(sr)
                ivcd.or_.append(gsc)
            if self.cur_tc.objectType:
                ivcd.nodetype.append = self.cur_tc.objectType
            if self.cur_tc.datatype:
                ivcd.datatype.append(self.cur_tc.datatype)
            self.cur_tc = None
        return ivcd

    def visitValueClassLabel(self, ctx: ShExDocParser.ValueClassLabelContext):
        # valueClassLabel : '$' iri ;
        return self.visit(ctx.iri())

    def visitBaseDecl(self, ctx: ShExDocParser.BaseDeclContext):
        # baseDecl : KW_BASE IRIREF
        self.base = self._iriref(ctx)

    def visitPrefixDecl(self, ctx: ShExDocParser.PrefixDeclContext):
        # prefixDecl : KW_PREFIX PNAME_NS IRIREF
        ns_txt = self._iriref(ctx)
        prefix = ctx.PNAME_NS().getText().split(':')[0]
        if prefix:
            self.nsc.declareNamespace(pyxb.namespace.Namespace(ns_txt), prefix)
            self.namespaces[prefix] = ns_txt
        else:
            self.nsc.setDefaultNamespace(pyxb.namespace.Namespace(ns_txt))
            self._schema.default_namespace = ns_txt

    def visitStart(self, ctx: ShExDocParser.StartContext):
        # start : KW_START '=' (shapeLabel | shapeDefinition semanticActions)
        if ctx.shapeLabel():
            self._schema.start = self.visit(ctx.shapeLabel())
        else:
            shape = self.visit(ctx.shapeDefinition())
            acts = self.visit(ctx.semanticActions())
            if acts:
                shape.actions = acts
            shape.label = "_:" + str(BNode())
            self._schema.start = shape.label
            self._schema.shape.append(shape)

    def visitShape(self, ctx: ShExDocParser.ShapeContext):
        # shape : KW_VIRTUAL? shapeLabel shapeDefinition semanticActions ;
        assert self.cur_shape is None, "Recursion error -- should be outermost shape"
        shape = self.visit(ctx.shapeDefinition())
        if ctx.KW_VIRTUAL():
            shape.virtual = True
        shape.label = self.visit(ctx.shapeLabel())
        acts = self.visit(ctx.semanticActions())
        if acts:
            shape.actions = acts
        self._schema.shape.append(shape)

    def visitShapeDefinition(self, ctx: ShExDocParser.ShapeDefinitionContext) -> Shape:
        # shapeDefinition : (includeSet | inclPropertySet | KW_CLOSED)* '{' someOfShape? '}' ;
        self._push_shape(Shape())
        # This is really screwey, as, on the shape definition label there are multiple sets of includes, while
        # on the tripleConstraint level there are just single includes.  We loose the "settiness" and make one
        # bit include set here
        if ctx.includeSet():
            [self.visit(c) for c in ctx.includeSet()]

        [self.visit(ips) for ips in ctx.inclPropertySet()]
        if ctx.KW_CLOSED():
            self.cur_shape.closed = True
        if ctx.someOfShape():
            self.visit(ctx.someOfShape())
        return self._pop_shape()

    def visitIncludeSet(self, ctx: ShExDocParser.IncludeSetContext):
        # includeSet : '&' shapeLabel+
        [self.cur_shape.import_.append(ShapeRef(ref=self.visit(sl))) for sl in ctx.shapeLabel()]

    def visitInclPropertySet(self, ctx: ShExDocParser.InclPropertySetContext):
        # inclPropertySet : KW_EXTRA predicate+
        self.cur_shape.extra += [IRIRef(ref=self.visit(p)) for p in ctx.predicate()]

    def visitSomeOfShape(self, ctx: ShExDocParser.SomeOfShapeContext):
        # someOfShape : groupShape | multiElementSomeOf
        self.visitChildren(ctx)

    # Visit a parse tree produced by ShExDocParser#multiElementSomeOf.
    def visitMultiElementSomeOf(self, ctx: ShExDocParser.MultiElementSomeOfContext) -> ShapeConstraint:
        # multiElementSomeOf : groupShape ( '|' groupShape)+ ;
        self._push_shape(ShapeConstraint())
        [self.visit(c) for c in ctx.groupShape()]
        rval = self._pop_shape()
        self._set_someof(rval)
        return rval

    # Visit a parse tree produced by ShExDocParser#innerShape.
    def visitInnerShape(self, ctx: ShExDocParser.InnerShapeContext):
        # innerShape : multiElementGroup | multiElementSomeOf ;
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShExDocParser#groupShape.
    def visitGroupShape(self, ctx: ShExDocParser.GroupShapeContext):
        # groupShape : singleElementGroup | multiElementGroup ;
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShExDocParser#singleElementGroup.
    def visitSingleElementGroup(self, ctx: ShExDocParser.SingleElementGroupContext):
        # singleElementGroup : unaryShape ','? ;
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShExDocParser#multiElementGroup.
    def visitMultiElementGroup(self, ctx: ShExDocParser.MultiElementGroupContext) -> ShapeConstraint:
        # multiElementGroup : unaryShape (',' unaryShape)+ ','? ;
        self._push_shape(ShapeConstraint())
        [self.visit(c) for c in ctx.unaryShape()]
        rval = self._pop_shape()
        self._set_group(rval)
        return rval

    def _proc_card_annot_semacts(self, target, ctx):
        """ Process cardinality, annotations and semantic actions for target
        :param target:
        :param ctx:
        :return:
        """
        self._cardinality(target, ctx)
        acts = self.visit(ctx.semanticActions())
        if acts:
            target.actions = acts
        [target.annotation.append(self.visit(a)) for a in ctx.annotation()]

    def visitUnaryShape(self, ctx: ShExDocParser.UnaryShapeContext):
        # unaryShape : tripleConstraint | include | encapsulatedShape ;
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ShExDocParser#encapsulatedShape.
    def visitEncapsulatedShape(self, ctx: ShExDocParser.EncapsulatedShapeContext):
        # encapsulatedShape : '(' innerShape ')' cardinality? annotation* semanticActions ;
        self._proc_card_annot_semacts(self.visit(ctx.innerShape()), ctx)

    def visitInclude(self, ctx: ShExDocParser.IncludeContext):
        # include : '&' shapeLabel
        self.cur_shape.include.append(ShapeRef(ref=self.visit(ctx.shapeLabel())))

    def visitShapeLabel(self, ctx: ShExDocParser.ShapeLabelContext) -> ShapeLabel:
        # shapeLabel : iri | blankNode
        return ShapeLabel(self.visitChildren(ctx))

    def visitTripleConstraint(self, ctx: ShExDocParser.TripleConstraintContext):
        # tripleConstraint : senseFlags? predicate valueClassOrRef cardinality? annotation* semanticActions;
        # senseFlags      : '!' '^'? | '^' '!'? ;
        tc = TripleConstraint()
        sf = self.visit(ctx.senseFlags()) if ctx.senseFlags() else ''
        if '!' in sf:
            tc.negated = True
        tc.predicate = self.visit(ctx.predicate())
        tc.reversed = '^' in sf
        if ctx.valueClassOrRef().valueClassLabel():
            tc.valueClass = self.visit(ctx.valueClassOrRef().valueClassLabel())
        else:
            parent_tc = self.cur_tc
            self.cur_tc = tc
            self.visit(ctx.valueClassOrRef().valueClass())
            self.cur_tc = parent_tc
        tc.__dict__.pop("reversed", None)
        self._proc_card_annot_semacts(tc, ctx)
        self._set_tc(tc)

    def visitSenseFlags(self, ctx: ShExDocParser.SenseFlagsContext):
        # senseFlags : '!' '^'? | '^' '!'? ;
        return ctx.getText()

    def visitPredicate(self, ctx: ShExDocParser.PredicateContext):
        # predicate : iri | rdfType ;
        if ctx.rdfType():
            return str(RDF.type)
        else:
            return self.visit(ctx.iri())

    def visitValueClassOrRef(self, ctx: ShExDocParser.ValueClassOrRefContext):
        # valueClassOrRef : valueClass | valueClassLabel ;
        # Note that valueClass isn't visited directly -- it is one of valueClassLiteral, valueClassNonLiteral, etc.
        assert False, "Should not be visited"

    def visitValueClassLiteral(self, ctx: ShExDocParser.ValueClassLiteralContext):
        # valueClass : KW_LITERAL xsFacet*
        self._subj_obj_type(NodeType.LITERAL)
        if ctx.xsFacet():
            vc = TripleConstraintValueClass()
            for f in ctx.xsFacet():
                vc.facet.append(self.visit(f))
            self._subj_obj_constraint(vc)

    def visitValueClassNonLiteral(self, ctx: ShExDocParser.ValueClassNonLiteralContext):
        # valueClass : (KW_IRI | KW_BNODE | KW_NONLITERAL) groupShapeConstr? stringFacet*
        self._subj_obj_type(NodeType.IRI if ctx.KW_IRI() else NodeType.BNODE if ctx.KW_BNODE() else NodeType.NONLITERAL)
        vc = None
        if ctx.groupShapeConstr():
            gsc = self.visit(ctx.groupShapeConstr())
            if len(gsc.disjunct) == 1:
                if self.cur_tc.reversed:
                    self.cur_tc.subjectShape = gsc.disjunct[0].ref
                else:
                    self.cur_tc.objectShape = gsc.disjunct[0].ref
            else:
                vc = TripleConstraintValueClass()
                vc.groupShapeConstr = gsc
        if ctx.stringFacet():
            if vc is None:
                vc = TripleConstraintValueClass()
            for sf in ctx.stringFacet():
                facet = XSFacet()
                self._proc_string_facet(facet, sf)
                vc.facet.append(facet)
        if vc is not None:
            self._subj_obj_constraint(vc)

    def visitValueClassDatatype(self, ctx: ShExDocParser.ValueClassDatatypeContext):
        # valueClass : datatype xsFacet*  # valueClassDatatype
        self.cur_tc.datatype = self.visit(ctx.datatype())
        if ctx.xsFacet():
            vc = TripleConstraintValueClass()
            for f in ctx.xsFacet():
                vc.facet.append(self.visit(f))
            self._subj_obj_constraint(vc)

    def visitValueClassGroup(self, ctx: ShExDocParser.ValueClassGroupContext):
        # valueClass : groupShapeConstr   # valueClassGroup
        gsc = self.visit(ctx.groupShapeConstr())
        if len(gsc.disjunct) == 1:
            if self.cur_tc.reversed:
                self.cur_tc.subjectShape = gsc.disjunct[0].ref
            else:
                self.cur_tc.objectShape = gsc.disjunct[0].ref
        else:
            vc = TripleConstraintValueClass()
            vc.or_ = gsc
            self._subj_obj_constraint(vc)

    def visitValueClassValueSet(self, ctx: ShExDocParser.ValueClassValueSetContext):
        # valueClass : valueSet  # valueClassValueSet
        # valueSet
        vs = self.visit(ctx.valueSet())

        # A single iri range without a stem maps to subject/object
        if vs.iriRange and len(vs.iriRange) == 1 and not vs.iriRange[0].exclusion and not vs.iriRange[0].stem:
            if self.cur_tc.reversed:
                self.cur_tc.subject = vs.iriRange[0].base
            else:
                self.cur_tc.object = vs.iriRange[0].base
        else:
            vc = TripleConstraintValueClass()
            vc.valueSet = vs
            self._subj_obj_constraint(vc)

    def visitValueClassAny(self, ctx: ShExDocParser.ValueClassAnyContext):
        # valueClass : '.'  # valueClassAny
        # Any is indicated by the lack fo constraints
        if self.cur_tc.reversed:
            self.cur_tc.inverse = True

    def visitGroupShapeConstr(self, ctx: ShExDocParser.GroupShapeConstrContext) -> GroupShapeConstr:
        # groupShapeConstr : shapeOrRef (KW_OR shapeOrRef)*
        rval = GroupShapeConstr()
        for sor in ctx.shapeOrRef():
            rval.disjunct.append(ShapeRef(ref=self.visit(sor)))
        return rval

    def visitShapeOrRef(self, ctx: ShExDocParser.ShapeOrRefContext) -> ShapeLabel:
        # shapeOrRef : ATPNAME_LN | ATPNAME_NS | '@' shapeLabel | shapeDefinition
        if ctx.shapeDefinition():
            shape = self.visit(ctx.shapeDefinition())
            shape.label = ShapeLabel('_:' + str(BNode()))
            self._schema.shape.append(shape)
            return shape.label
        elif ctx.shapeLabel():
            return self.visit(ctx.shapeLabel())
        elif ctx.ATPNAME_LN():
            return ShapeLabel(ctx.ATPNAME_LN().getText()[1:])    # strip the leading @
        else:
            return ShapeLabel(ctx.ATPNAME_NS().getText()[1:-1])  # strip the @ and trailing :

    def visitXsFacet(self, ctx: ShExDocParser.XsFacetContext) -> XSFacet:
        # xsFacet : stringFacet | numericFacet
        rval = XSFacet()
        if ctx.stringFacet():
            return self._proc_string_facet(rval, ctx.stringFacet())
        else:
            self._proc_numeric_facet(rval, ctx.numericFacet())
        return rval

    def visitStringFacet(self, ctx: ShExDocParser.StringFacetContext):
        # stringFacet : KW_PATTERN string | '~' string | stringLength INTEGER |
        return self._proc_string_facet(StringFacet(), ctx)

    def visitStringLength(self, ctx: ShExDocParser.StringLengthContext):
        # stringLength	: KW_LENGTH | KW_MINLENGTH | KW_MAXLENGTH;
        # Not visited -- handled above
        return self.visitChildren(ctx)

    def visitNumericFacet(self, ctx: ShExDocParser.NumericFacetContext) -> NumericFacet:
        # numericFacet : numericRange INTEGER | numericLength INTEGER
        return self._proc_numeric_facet(NumericFacet(), ctx)

    def visitNumericRange(self, ctx: ShExDocParser.NumericRangeContext):
        # numericRange : KW_MININCLUSIVE | KW_MINEXCLUSIVE | KW_MAXINCLUSIVE | KW_MAXEXCLUSIVE ;
        # Not visited -- handled above
        return self.visitChildren(ctx)

    def visitNumericLength(self, ctx: ShExDocParser.NumericLengthContext):
        # numericLength   : KW_TOTALDIGITS | KW_FRACTIONDIGITS ;
        # not visited - handled above
        return self.visitChildren(ctx)

    def visitDatatype(self, ctx: ShExDocParser.DatatypeContext):
        # datatype : iri ;
        return self.visitChildren(ctx)

    def visitAnnotation(self, ctx: ShExDocParser.AnnotationContext) -> Annotation:
        # annotation : ';' predicate (iri | literal) ;
        rval = Annotation()
        rval.iri = self.visit(ctx.predicate())
        if ctx.literal():
            lit = self.visit(ctx.literal())
            if not ctx.literal().rdfLiteral():
                lit = RDFLiteral(lit)
            rval.literal = lit
        else:
            rval.iriref = IRIRef(ref=self.visit(ctx.iri()))
        return rval

    def visitCardinality(self, ctx: ShExDocParser.CardinalityContext) -> list:
        # cardinality : '*' | '+' | '?' | repeatRange ;
        if not ctx:
            return [1, 1]
        elif ctx.repeatRange():
            return self.visitRepeatRange(ctx.repeatRange())
        elif ctx.getText() == '*':
            return [0, None]
        elif ctx.getText() == '+':
            return [1, None]
        else:
            assert ctx.getText() == '?', "Unknown cardinality character"
            return [0, 1]

    # returns [min_range, max_range or None]
    def visitRepeatRange(self, ctx: ShExDocParser.RepeatRangeContext) -> list:
        # repeatRange : '{' min_range ( ',' max_range?)? '}' ;
        minr = self.visit(ctx.min_range())
        maxr = self.visit(ctx.max_range()) if ctx.max_range() else None if ctx.getChild(2).getText() == ',' else minr
        return [minr, maxr]

    def visitMin_range(self, ctx: ShExDocParser.Min_rangeContext):
        # min_range : INTEGER ;
        return int(ctx.INTEGER().getText())

    def visitMax_range(self, ctx: ShExDocParser.Max_rangeContext):
        # max_range : INTEGER | '*' ;
        return int(ctx.INTEGER().getText()) if ctx.INTEGER() else None

    # returns ValueSet or IRIRef
    def visitValueSet(self, ctx: ShExDocParser.ValueSetContext):
        # value    : '(' value* ')' ;
        vs = ValueSet()
        for v in ctx.value():
            val = self.visit(v)
            if v.iriRange():
                vs.iriRange.append(val)
            elif v.literal().rdfLiteral():
                vs.rdfLiteral.append(val)
            elif v.literal().numericLiteral():
                if v.literal().numericLiteral().DECIMAL():
                    vs.decimal.append(val.decimal)
                elif v.literal().numericLiteral().INTEGER():
                    vs.integer.append(val.integer)
                else:
                    vs.double.append(val.double)
            else:
                vs.boolean.append(val)
        return vs

    def visitValue(self, ctx: ShExDocParser.ValueContext):
        # value : iriRange | literal
        return self.visitChildren(ctx)

    def visitIriRange(self, ctx: ShExDocParser.IriRangeContext) -> IRIRange:
        # iriRange : iri ('~' exclusion*)? | '.' exclusion+
        rval = IRIRange()
        if ctx.iri():
            rval.base = self.visit(ctx.iri())
            if ctx.getChildCount() > 1 and str(ctx.getChild(1) == '~'):
                rval.stem = True
        for e in ctx.exclusion():
            rval.exclusion.append(self.visit(e))
        return rval

    def visitExclusion(self, ctx: ShExDocParser.ExclusionContext) -> IRIStem:
        # exclusion : '-' iri '~'?
        rval = IRIStem(base=self.visit(ctx.iri()))
        if ctx.getChildCount() > 2:
            assert str(ctx.getChild(2)) == '~', "Expecting stem (~) instruction"
            rval.stem = True
        return rval

    def visitLiteral(self, ctx: ShExDocParser.LiteralContext):
        # literal : rdfLiteral | numericLiteral | booleanLiteral ;
        return self.visitChildren(ctx)

    def visitNumericLiteral(self, ctx: ShExDocParser.NumericLiteralContext):
        # numericLiteral  : INTEGER | DECIMAL | DOUBLE ;
        return self._proc_numeric_literal(NumericLiteral(), ctx)

    def visitRdfLiteral(self, ctx: ShExDocParser.RdfLiteralContext) -> RDFLiteral:
        # rdfLiteral : string (LANGTAG | '^^' datatype)? ;
        rval = RDFLiteral(self.visit(ctx.string()))
        if ctx.LANGTAG():
            rval.langtag = ctx.LANGTAG().getText()[1:]
        elif ctx.datatype():
            rval.datatype = self.visit(ctx.datatype())
        return rval

    def visitBooleanLiteral(self, ctx: ShExDocParser.BooleanLiteralContext) -> bool:
        # booleanLiteral : KW_TRUE | KW_FALSE
        return bool(ctx.KW_TRUE())

    def visitString(self, ctx: ShExDocParser.StringContext):
        # string : STRING_LITERAL1
        # 	| STRING_LITERAL2
        # 	| STRING_LITERAL_LONG1
        # 	| STRING_LITERAL_LONG2
        if ctx.STRING_LITERAL1() or ctx.STRING_LITERAL2():
            return ctx.getText()[1:-1]
        else:
            return ctx.getText()[3:-3]

    def visitIri(self, ctx: ShExDocParser.IriContext):
        # iri : IRIREF | prefixedName ;
        if ctx.IRIREF():
            return self._iriref(ctx)
        else:
            return escape(self.visitChildren(ctx))

    def visitPrefixedName(self, ctx: ShExDocParser.PrefixedNameContext) -> str:
        # prefixedName : PNAME_LN | PNAME_NS ;
        #
        # includes: "ns:", ":foo" and "ns:foo"
        return ctx.getText()

    # Visit a parse tree produced by ShExDocParser#blankNode.
    def visitBlankNode(self, ctx: ShExDocParser.BlankNodeContext) -> str:
        # blankNode       : BLANK_NODE_LABEL
        return ctx.getText()

    def visitCodeDecl(self, ctx: ShExDocParser.CodeDeclContext) -> SemanticAction:
        # codeDecl : '%' (productionName | iri? CODE?) ;
        # CODE : '{' (~[%\\] | '\\%')* '%' '}' ;
        action = SemanticAction()
        if ctx.productionName():
            action.productionName = self.visit(ctx.productionName())
        else:
            action.codeDecl = CodeDecl(ctx.CODE().getText()[1:-2])
            if ctx.iri():
                NamespaceContext.PushContext(self.nsc)
                action.codeDecl.iri = self.visit(ctx.iri())
        return action

    def _proc_actions(self, ctx) -> SemanticActions:
        rval = SemanticActions()
        for dcl in ctx.codeDecl():
            rval.action.append(self.visit(dcl))
        return rval

    def visitProductionName(self, ctx: ShExDocParser.ProductionNameContext) -> str:
        # productionName : UCASE_LABEL ;
        return ProductionName(ref=ctx.UCASE_LABEL().getText())

    def visitStartActions(self, ctx: ShExDocParser.StartActionsContext) -> SemanticActions:
        # startActions : codeDecl+
        self._schema.startActions = self._proc_actions(ctx)

    def visitSemanticActions(self, ctx: ShExDocParser.SemanticActionsContext) -> SemanticActions:
        # semanticActions : codeDecl*
        if ctx.codeDecl():
            return self._proc_actions(ctx)
        else:
            return None

    def visitRdfType(self, ctx:ShExDocParser.RdfTypeContext):
        return str(RDF.type)

    # ---------------------------------------
    # Support methods
    # ----------------------------------------
    def _push_shape(self, new_shape):
        # Push the current shape being process and set the current shape to new_shape
        self.shape_stack.append(self.cur_shape)
        self.cur_shape = new_shape

    def _pop_shape(self):
        # Return the current shape and replace it with the top of the shape stack
        # NOTE: self.cur_shape.foo.append(self._pop_shape()) doesn't work!
        rval = self.cur_shape
        self.cur_shape = self.shape_stack.pop()
        return rval

    def _iriref(self, ctx):
        """ Parse a uri in the form "<iri>"
        :param ctx: container with an IRIREF inside
        :return: absolute URI
        """
        return urljoin(self.base, escape(ctx.IRIREF().getText()[1:-1]), allow_fragments=False)

    def _cardinality(self, container, ctx):
        minr, maxr = self.visitCardinality(ctx.cardinality())
        if minr != 1:
            container.min = minr
        if maxr != 1:
            container.max = maxr if maxr else "unbounded"

    def _subj_obj_type(self, node_type: NodeType):
        if self.cur_tc.reversed:
            self.cur_tc.subjectType = node_type
        else:
            self.cur_tc.objectType = node_type

    def _subj_obj_constraint(self, vc: TripleConstraintValueClass):
        if self.cur_tc.reversed:
            self.cur_tc.subjectConstraint = vc
        else:
            self.cur_tc.objectConstraint = vc

    def _proc_numeric_facet(self, target, ctx: ShExDocParser.NumericFacetContext) -> NumericFacet:
        if ctx.numericLength():
            val = ctx.INTEGER().getText()
            if ctx.numericLength().KW_TOTALDIGITS():
                target.totalDigits = val
            else:
                target.fractionDigits = val
        else:
            val = self._proc_numeric_literal(EndPoint(), ctx.numericLiteral())
            if ctx.numericRange().KW_MININCLUSIVE():
                target.minValue = val
            elif ctx.numericRange().KW_MINEXCLUSIVE():
                val.open = True
                target.minValue = val
            elif ctx.numericRange().KW_MAXINCLUSIVE():
                target.maxValue = val
            else:
                val.open = True
                target.maxValue = val
        return target

    @staticmethod
    def _proc_numeric_literal(target: NumericLiteral, ctx: ShExDocParser.NumericLiteralContext) -> NumericLiteral:
        if ctx.INTEGER():
            target.integer = datatypes.int(ctx.INTEGER().getText())
        elif ctx.DECIMAL():
            target.decimal = datatypes.decimal(ctx.DECIMAL().getText())
        else:
            target.double = datatypes.double(ctx.DOUBLE().getText())
        return target

    def _proc_string_facet(self, target, ctx: ShExDocParser.StringFacetContext) -> NumericFacet:
        if ctx.stringLength():
            intval = int(ctx.INTEGER().getText())
            if ctx.stringLength().KW_LENGTH():
                target.length = intval
            elif ctx.stringLength().KW_MINLENGTH():
                target.minLength = intval
            elif ctx.stringLength().KW_MAXLENGTH():
                target.maxLength = intval
            else:
                assert False, "Unrecognized stringlength facet"
        else:
            if ctx.getChild(0).getText() == '~':
                target.not_ = self.visit(ctx.string())
            else:
                target.pattern = self.visit(ctx.string())
        return target

    def _set_someof(self, v):
        if isinstance(self.cur_shape.someOf, Iterable):
            self.cur_shape.someOf.append(v)
        else:
            self.cur_shape.someOf = v

    def _set_group(self, v):
        if isinstance(self.cur_shape.group, Iterable):
            self.cur_shape.group.append(v)
        else:
            self.cur_shape.group = v

    def _set_tc(self, v):
        if isinstance(self.cur_shape.tripleConstraint, Iterable):
            self.cur_shape.tripleConstraint.append(v)
        else:
            self.cur_shape.tripleConstraint = v
