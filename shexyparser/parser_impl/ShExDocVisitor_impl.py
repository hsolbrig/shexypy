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
from rdflib import RDF, BNode
from pyxb.utils import domutils
from pyxb.namespace import XMLSchema_instance as xsi, NamespaceContext
from pyxb.namespace import XMLNamespaces as xmlns
from urllib.parse import urljoin

if not globals().get("__package__", None):
    from ShExDocParser import ShExDocParser
    from ShExDocVisitor import ShExDocVisitor
else:
    from shexyparser.parser.ShExDocVisitor import ShExDocVisitor
    from shexyparser.parser.ShExDocParser import ShExDocParser

from shexyparser.schema.ShEx import *
exclude_namespaces = ['xsi', 'shex']


class ShExDocVisitor_impl(ShExDocVisitor):
    def __init__(self):
        ShExDocVisitor.__init__(self)
        self._schema = None
        self.base = ""
        self.cur_shape = None            # current working shape definition
        self.cur_tc = None               # current working triple constraint definition
        self.namespaces = {}
        dns = pyxb.namespace.CreateAbsentNamespace()
        self.nsc = pyxb.namespace.NamespaceContext(target_namespace=dns)

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
                                    'file:/Users/mrf7578/Development/git/hsolbrig/shexypy/static/xsd/ShEx.xsd')
        schema_dom.documentElement.setAttributeNS(xmlns.uri, 'xmlns:xsi', xsi.uri())
        return schema_dom

    def _iriref(self, ctx):
        return urljoin(self.base, ctx.IRIREF().getText()[1:-1])

    @property
    def schema(self):
        return self._schema

    def visitShExDoc(self, ctx: ShExDocParser.ShExDocContext) -> Schema:
        # shExDoc : directive* ((shape | start | valueClassDefinition | startActions) statement*)? EOF;
        self._schema = Schema()
        Namespace.setPrefix(prefix="shex")
        pyxb.defaultNamespace = Namespace
        self.visitChildren(ctx)
        return self

    def visitStatement(self, ctx: ShExDocParser.StatementContext):
        # statement	: directive | start | shape | valueClassDefinition ;
        return self.visitChildren(ctx)

    def visitDirective(self, ctx: ShExDocParser.DirectiveContext):
        # directive       : baseDecl | prefixDecl ;
        return self.visitChildren(ctx)

    def visitValueClassDefinition(self, ctx: ShExDocParser.ValueClassDefinitionContext):
        # valueClassDefinition : valueClassLabel ('=' valueClassExpr semanticActions | KW_EXTERNAL) ;
        return self.visitChildren(ctx)

    def visitValueClassExpr(self, ctx: ShExDocParser.ValueClassExprContext):
        # valueClassExpr  : valueClass ('+' valueClass)* ;
        return self.visitChildren(ctx)

    def visitValueClassLabel(self, ctx: ShExDocParser.ValueClassLabelContext):
        # valueClassLabel : '$' iri ;
        return self.visitChildren(ctx)

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
            self._add_actions(shape, ctx)
            shape.label = str(BNode())
            self._schema.start = shape.label
            self._schema.shape.append(shape)

    def visitShape(self, ctx: ShExDocParser.ShapeContext):
        # shape : KW_VIRTUAL? shapeLabel shapeDefinition semanticActions ;
        shape = self.visit(ctx.shapeDefinition())
        if ctx.KW_VIRTUAL():
            shape.virtual = True
        shape.label = self.visit(ctx.shapeLabel())
        self._add_actions(shape, ctx)
        self._schema.shape.append(shape)

    def _add_actions(self, target, ctx):
        if ctx.semanticActions():
            actns = self.visit(ctx.semanticActions())
            if actns:
                target.semanticActions = actns

    def visitShapeDefinition(self, ctx: ShExDocParser.ShapeDefinitionContext) -> Shape:
        # shapeDefinition : (includeSet | inclPropertySet | KW_CLOSED)* '{' someOfShape? '}' ;
        assert self.cur_shape is None, "Recursion error -- should be outermost shape"
        self.cur_shape = Shape()
        for e in ctx.includeSet():
            self.visit(e)
        for ips in ctx.inclPropertySet():
            self.visit(ips)
        if ctx.KW_CLOSED():
            self.cur_shape.closed = True
        if ctx.someOfShape():
            self.visit(ctx.someOfShape())
        rval = self.cur_shape
        self.cur_shape = None
        return rval

    def visitIncludeSet(self, ctx: ShExDocParser.IncludeSetContext):
        # includeSet : '&' shapeLabel+
        self.cur_shape.include.append(IncludeShape(ref=self.visit(ctx.shapeLabel())))

    def visitInclPropertySet(self, ctx: ShExDocParser.InclPropertySetContext):
        # inclPropertySet : KW_EXTRA predicate+
        self.cur_shape.extra += [IncludeProperty(ref=self.visit(p)) for p in ctx.predicate()]

    def _one_or_many(self, children, attach_to):
        """ If there is one child, attach it directly to the parent shape.  Otherwise, create an inner
        ShapeConstraint and attach it to the appropriate (oneOf, someOf, group) node
        :param children: set of children to process
        :param attach_to: node to attach the inner constraint to
        """
        if len(children) > 1:
            parent_shape = self.cur_shape
            self.cur_shape = ShapeConstraint()
            for c in children:
                self.visit(c)
            attach_to.append(self.cur_shape)
            self.cur_shape = parent_shape
        else:
            self.visit(children[0])

    def visitSomeOfShape(self, ctx: ShExDocParser.SomeOfShapeContext):
        # someOfShape : groupShape ( '||' groupShape) *
        self._one_or_many(ctx.groupShape(), self.cur_shape.someOf)

    def visitGroupShape(self, ctx: ShExDocParser.GroupShapeContext):
        # groupShape : unaryShape ( ',' unaryShape )* ','? ;
        self._one_or_many(ctx.unaryShape(), self.cur_shape.group)

    def visitUnaryShape(self, ctx: ShExDocParser.UnaryShapeContext):
        # unaryShape : shapeid? ( tripleConstraint | include | '(' oneOfShape ')' cardinality? semanticActions) ;
        # unaryShape has no equivalent in the XML, as it is always a single container
        if ctx.tripleConstraint() or ctx.include():
            self.visitChildren(ctx)
        else:
            parent_shape = self.cur_shape
            self.cur_shape = ShapeConstraint()
            self.visit(ctx.someOfShape())
            self._cardinality(self.cur_shape, ctx)
            self._add_actions(self.cur_shape, ctx)
            parent_shape.group.append(self.cur_shape)
            self.cur_shape = parent_shape

    def visitInclude(self, ctx: ShExDocParser.IncludeContext):
        # include : '&' shapeLabel+
        self.cur_shape.include.append(self.visit(ctx.shapeLabel()))

    def visitShapeLabel(self, ctx: ShExDocParser.ShapeLabelContext) -> ShapeLabel:
        # shapeLabel : iri | blankNode
        return ShapeLabel(self.visitChildren(ctx))

    def visitTripleConstraint(self, ctx: ShExDocParser.TripleConstraintContext):
        # tripleConstraint : senseFlags? predicate valueClassOrRef cardinality? annotation* semanticActions;
        # senseFlags      : '!' '^'? | '^' '!'? ;
        tc = TripleConstraint()
        tc.reversed = ctx.senseFlags() and '^' in ctx.senseFlags().getText()
        if ctx.senseFlags() and '!' in ctx.senseFlags().getText():
            tc.negated = True
        tc.predicate = self.visit(ctx.predicate())
        self._cardinality(tc, ctx)
        for e in ctx.annotation():
            tc.annotation.append(self.visit(e))
        self._add_actions(tc, ctx)
        parent_tc = self.cur_tc
        self.cur_tc = tc
        self.visit(ctx.valueClassOrRef())
        self.cur_tc = parent_tc
        tc.__dict__.pop('reversed', None)
        self.cur_shape.tripleConstraint.append(tc)

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

    def _subj_obj_constraint(self, vc: ValueClass):
        if self.cur_tc.reversed:
            self.cur_tc.subjectConstraint = vc
        else:
            self.cur_tc.objectConstraint = vc

    def visitSenseFlags(self, ctx: ShExDocParser.SenseFlagsContext):
        # senseFlags : '!' '^'? | '^' '!'? ;
        return self.visitChildren(ctx)

    def visitPredicate(self, ctx: ShExDocParser.PredicateContext):
        # predicate : iri | RDF_TYPE ;
        if ctx.RDF_TYPE():
            return str(RDF.type)
        else:
            return self.visitChildren(ctx)

    def visitValueClassOrRef(self, ctx: ShExDocParser.ValueClassOrRefContext):
        # valueClassOrRef : valueClass | valueClassLabel ;
        return self.visitChildren(ctx)

    def visitValueClassLiteral(self, ctx: ShExDocParser.ValueClassLiteralContext):
        # valueClass : KW_LITERAL xsFacet*
        self._subj_obj_type(NodeType.LITERAL)
        if ctx.xsFacet():
            vc = ValueClass()
            for f in ctx.xsFacet():
                vc.facet.append(self.visit(f))
            self._subj_obj_constraint(vc)

    def visitValueClassNonLiteral(self, ctx: ShExDocParser.ValueClassNonLiteralContext):
        # valueClass : (KW_IRI | KW_BNODE | KW_NONLITERAL) groupShapeConstr? stringFacet*
        self._subj_obj_type(NodeType.IRI if ctx.KW_IRI() else NodeType.BNODE if ctx.KW_BNODE() else NodeType.NONLITERAL)
        if ctx.groupShapeConstr():
            gsc = self.visit(ctx.groupShapeConstr())
            if len(gsc.groupShapeConstr) == 1:
                if self.cur_tc.reversed:
                    self.cur_tc.subjectShape = gsc.groupShapeConstr[0].ref
                else:
                    self.cur_tc.objectShape = gsc.groupShapeConstr[0].ref
                gsc.groupShapeConstr.pop()
            if gsc.groupShapeConstr or gsc.stringFacet:
                vc = ValueClass()
                vc.groupShapeConstr = gsc
                self._subj_obj_constraint(vc)

    def visitValueClassDatatype(self, ctx: ShExDocParser.ValueClassDatatypeContext):
        # valueClass : datatype xsFacet*  # valueClassDatatype
        self.cur_tc.datatype = self.visit(ctx.datatype())
        if ctx.xsFacet():
            vc = ValueClass()
            for f in ctx.xsFacet():
                vc.facet.append(self.visit(f))
            self._subj_obj_constraint(vc)

    def visitValueClassGroup(self, ctx: ShExDocParser.ValueClassGroupContext):
        # valueClass : groupShapeConstr   # valueClassGroup
        gsc = self.visit(ctx.groupShapeConstr())
        if len(gsc.groupShapeConstr) == 1:
            if self.cur_tc.reversed:
                self.cur_tc.subjectShape = gsc.groupShapeConstr[0].ref
            else:
                self.cur_tc.objectShape = gsc.groupShapeConstr[0].ref
        else:
            vc = ValueClass()
            vc.groupShapeConstr = gsc
            self._subj_obj_constraint(vc)

    def visitValueClassValueSet(self, ctx: ShExDocParser.ValueClassValueSetContext):
        # valueClass : valueSet  # valueClassValueSet
        vs_or_vsr = self.visit(ctx.valueSet())
        if isinstance(vs_or_vsr, ValueSet):
            if vs_or_vsr.iriRange and len(vs_or_vsr.iriRange) == 1 and not vs_or_vsr.iriRange[0].exclusion:
                if self.cur_tc.reversed:
                    self.cur_tc.subject = vs_or_vsr.iriRange[0].base
                else:
                    self.cur_tc.object = vs_or_vsr.iriRange[0].base
            else:
                vc = ValueClass()
                # TODO: THis is not correct -- where is the cardinality?
                vc.valueSet.append(vs_or_vsr)
                self._subj_obj_constraint(vc)
        else:
            assert isinstance(vs_or_vsr, IRIRef), "Parser / model mismatch"
            vc = ValueClass()
            vc.valueSetReference = vs_or_vsr
            self._subj_obj_constraint(vc)

    def visitValueClassAny(self, ctx: ShExDocParser.ValueClassAnyContext):
        # valueClass : '.'  # valueClassAny
        # Any is indicated by the lack fo constraints
        pass

    def visitGroupShapeConstr(self, ctx: ShExDocParser.GroupShapeConstrContext) -> GroupShapeConstr:
        # groupShapeConstr : shapeOrRef (KW_OR shapeOrRef)*
        rval = GroupShapeConstr()
        for sor in ctx.shapeOrRef():
            rval.groupShapeConstr.append(ShapeRef(ref=self.visit(sor)))
        return rval

    def visitShapeOrRef(self, ctx: ShExDocParser.ShapeOrRefContext) -> ShapeLabel:
        # shapeOrRef : ATPNAME_LN | ATPNAME_NS | '@' shapeLabel | shapeDefinition
        if ctx.shapeDefinition():
            shape = self.visit(ctx.shapeDefinition())
            shape.label = ShapeLabel(str(BNode()))
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

    @staticmethod
    def _proc_numeric_facet(target, ctx: ShExDocParser.NumericFacetContext) -> NumericFacet:
        val = ctx.INTEGER().getText()
        if ctx.numericLength():
            if ctx.numericLength().KW_TOTALDIGITS():
                target.totalDigits = val
            else:
                target.fractionDigits = val
        else:
            if ctx.numericRange().KW_MININCLUSIVE():
                target.minValue = Range(val)
            elif ctx.numericRange().KW_MINEXCLUSIVE():
                target.minValue = Range(val, open=True)
            elif ctx.numericRange().KW_MAXINCLUSIVE():
                target.maxValue = Range(val)
            else:
                target.maxValue = Range(val, open=True)
        return target

    @staticmethod
    def _proc_string_facet(target, ctx: ShExDocParser.StringFacetContext) -> NumericFacet:
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
            target.pattern = ctx.string().getText()
        return target

    def visitStringFacet(self, ctx: ShExDocParser.StringFacetContext):
        # stringFacet : stringLength INTEGER | KW_PATTERN string | '~' string
        return self._proc_string_facet(StringFacet(), ctx)

    def visitStringLength(self, ctx: ShExDocParser.StringLengthContext):
        # stringLength	: KW_LENGTH | KW_MINLENGTH | KW_MAXLENGTH;
        # Not visited -- handled above
        return self.visitChildren(ctx)

    def visitNumericFacet(self, ctx: ShExDocParser.NumericFacetContext) -> NumericFacet:
        # numericFacet	: numericRange INTEGER | numericLength INTEGER
        return self._proc_numeric_facet(NumericFacet(), ctx)

    def visitNumericRange(self, ctx: ShExDocParser.NumericRangeContext):
        # numericRange	: KW_MININCLUSIVE | KW_MINEXCLUSIVE | KW_MAXINCLUSIVE | KW_MAXEXCLUSIVE ;
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
        # annotation : ';' iri (iri | literal) ;
        rval = Annotation()
        rval.iri = self.visit(ctx.iri(0))
        if ctx.literal():
            rval.literal = self.visit(ctx.literal())
        else:
            rval.iriref = self.visit(ctx.iri(1))
        return rval

    def visitCardinality(self, ctx: ShExDocParser.CardinalityContext) -> list:
        # cardinality : '*' | '+' | '?' | repeatRange
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

    def visitRepeatRange(self, ctx: ShExDocParser.RepeatRangeContext) -> list:
        # repeatRange : '{' INTEGER ( ',' (INTEGER | '*')?)? '}'
        minr = int(ctx.INTEGER(0).getText())
        return [minr, minr if str(ctx.getChild(2)) == '}' else
                      None if str(ctx.getChild(3)) == '}' else
                      int(ctx.INTEGER(1).getText())]

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
                    vs.decimal.append(val)
                elif v.literal().numericLiteral().INTEGER():
                    vs.integer.append(val)
                else:
                    vs.double.append(val)
            else:
                vs.boolean.append(val)
        return vs

    def visitValue(self, ctx: ShExDocParser.ValueContext):
        # value : iriRange | literal
        return self.visitChildren(ctx)

    def visitIriRange(self, ctx: ShExDocParser.IriRangeContext) -> IRIRange:
        # iriRange : iri ('~' exclusion*)?
        rval = IRIRange(base=self.visit(ctx.iri()))
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

    def visitLiteral(self, ctx):
        return self.visitChildren(ctx)

    def visitNumericLiteral(self, ctx):
        return self.visitChildren(ctx)

    def visitRdfLiteral(self, ctx: ShExDocParser.RdfLiteralContext) -> RDFLiteral:
        rval = RDFLiteral(self.visit(ctx.string()))
        if ctx.LANGTAG():
            rval.langtag = ctx.LANGTAG().getText()
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
            return self.visit(ctx).getText()[1:-1]
        else:
            return self.visit(ctx).getText()[3:-3]

    def visitIri(self, ctx: ShExDocParser.IriContext):
        # iri : IRIREF | prefixedName
        if ctx.IRIREF():
            return ctx.IRIREF().getText()
        else:
            return self.visitChildren(ctx)

    def visitPrefixedName(self, ctx: ShExDocParser.PrefixedNameContext) -> str:
        # prefixedName : PNAME_LN
        #              : PNAME_NS
        #
        # includes: "ns:", ":foo" and "ns:foo"
        return ctx.getText()

    # Visit a parse tree produced by ShExDocParser#blankNode.
    def visitBlankNode(self, ctx: ShExDocParser.BlankNodeContext) -> str:
        # blankNode       : BLANK_NODE_LABEL
        return ctx.getText()

    def visitCodeDecl(self, ctx: ShExDocParser.CodeDeclContext) -> SemanticAction:
        # codeDecl : '%' (codeLabel | iri? CODE?) ;
        # CODE : '{' (~[%\\] | '\\%')* '%' '}' ;
        action = SemanticAction()
        if ctx.codeLabel():
            action.codeLabel = self.visit(ctx.codeLabel())
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

    def visitCodeLabel(self, ctx: ShExDocParser.CodeLabelContext) -> str:
        # codeLabel : UCASE_LABEL ;
        return CodeLabel(ref=ctx.UCASE_LABEL().getText())

    def visitStartActions(self, ctx: ShExDocParser.StartActionsContext) -> SemanticActions:
        # startActions : codeDecl+
        self._schema.startActions = self._proc_actions(ctx)

    def visitSemanticActions(self, ctx: ShExDocParser.SemanticActionsContext) -> SemanticActions:
        # semanticActions : codeDecl*
        if ctx.codeDecl():
            return self._proc_actions(ctx)
        else:
            return None
