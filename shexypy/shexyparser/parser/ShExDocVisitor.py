# Generated from ShExDoc.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ShExDocParser import ShExDocParser
else:
    from ShExDocParser import ShExDocParser

# This class defines a complete generic visitor for a parse tree produced by ShExDocParser.

class ShExDocVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ShExDocParser#shExDoc.
    def visitShExDoc(self, ctx:ShExDocParser.ShExDocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#statement.
    def visitStatement(self, ctx:ShExDocParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#notStartAction.
    def visitNotStartAction(self, ctx:ShExDocParser.NotStartActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#directive.
    def visitDirective(self, ctx:ShExDocParser.DirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassDefinition.
    def visitValueClassDefinition(self, ctx:ShExDocParser.ValueClassDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassExpr.
    def visitValueClassExpr(self, ctx:ShExDocParser.ValueClassExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassLabel.
    def visitValueClassLabel(self, ctx:ShExDocParser.ValueClassLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#baseDecl.
    def visitBaseDecl(self, ctx:ShExDocParser.BaseDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#prefixDecl.
    def visitPrefixDecl(self, ctx:ShExDocParser.PrefixDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#start.
    def visitStart(self, ctx:ShExDocParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#shape.
    def visitShape(self, ctx:ShExDocParser.ShapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#shapeDefinition.
    def visitShapeDefinition(self, ctx:ShExDocParser.ShapeDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#includeSet.
    def visitIncludeSet(self, ctx:ShExDocParser.IncludeSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#inclPropertySet.
    def visitInclPropertySet(self, ctx:ShExDocParser.InclPropertySetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#someOfShape.
    def visitSomeOfShape(self, ctx:ShExDocParser.SomeOfShapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#multiElementSomeOf.
    def visitMultiElementSomeOf(self, ctx:ShExDocParser.MultiElementSomeOfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#innerShape.
    def visitInnerShape(self, ctx:ShExDocParser.InnerShapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#groupShape.
    def visitGroupShape(self, ctx:ShExDocParser.GroupShapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#singleElementGroup.
    def visitSingleElementGroup(self, ctx:ShExDocParser.SingleElementGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#multiElementGroup.
    def visitMultiElementGroup(self, ctx:ShExDocParser.MultiElementGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#unaryShape.
    def visitUnaryShape(self, ctx:ShExDocParser.UnaryShapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#encapsulatedShape.
    def visitEncapsulatedShape(self, ctx:ShExDocParser.EncapsulatedShapeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#include.
    def visitInclude(self, ctx:ShExDocParser.IncludeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#shapeLabel.
    def visitShapeLabel(self, ctx:ShExDocParser.ShapeLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#tripleConstraint.
    def visitTripleConstraint(self, ctx:ShExDocParser.TripleConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#senseFlags.
    def visitSenseFlags(self, ctx:ShExDocParser.SenseFlagsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#predicate.
    def visitPredicate(self, ctx:ShExDocParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassOrRef.
    def visitValueClassOrRef(self, ctx:ShExDocParser.ValueClassOrRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassLiteral.
    def visitValueClassLiteral(self, ctx:ShExDocParser.ValueClassLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassNonLiteral.
    def visitValueClassNonLiteral(self, ctx:ShExDocParser.ValueClassNonLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassDatatype.
    def visitValueClassDatatype(self, ctx:ShExDocParser.ValueClassDatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassGroup.
    def visitValueClassGroup(self, ctx:ShExDocParser.ValueClassGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassValueSet.
    def visitValueClassValueSet(self, ctx:ShExDocParser.ValueClassValueSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassAny.
    def visitValueClassAny(self, ctx:ShExDocParser.ValueClassAnyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#groupShapeConstr.
    def visitGroupShapeConstr(self, ctx:ShExDocParser.GroupShapeConstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#shapeOrRef.
    def visitShapeOrRef(self, ctx:ShExDocParser.ShapeOrRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#xsFacet.
    def visitXsFacet(self, ctx:ShExDocParser.XsFacetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#stringFacet.
    def visitStringFacet(self, ctx:ShExDocParser.StringFacetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#stringLength.
    def visitStringLength(self, ctx:ShExDocParser.StringLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#numericFacet.
    def visitNumericFacet(self, ctx:ShExDocParser.NumericFacetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#numericRange.
    def visitNumericRange(self, ctx:ShExDocParser.NumericRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#numericLength.
    def visitNumericLength(self, ctx:ShExDocParser.NumericLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#datatype.
    def visitDatatype(self, ctx:ShExDocParser.DatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#annotation.
    def visitAnnotation(self, ctx:ShExDocParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#cardinality.
    def visitCardinality(self, ctx:ShExDocParser.CardinalityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#repeatRange.
    def visitRepeatRange(self, ctx:ShExDocParser.RepeatRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#min_range.
    def visitMin_range(self, ctx:ShExDocParser.Min_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#max_range.
    def visitMax_range(self, ctx:ShExDocParser.Max_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueSet.
    def visitValueSet(self, ctx:ShExDocParser.ValueSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#value.
    def visitValue(self, ctx:ShExDocParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#iriRange.
    def visitIriRange(self, ctx:ShExDocParser.IriRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#exclusion.
    def visitExclusion(self, ctx:ShExDocParser.ExclusionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#literal.
    def visitLiteral(self, ctx:ShExDocParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#numericLiteral.
    def visitNumericLiteral(self, ctx:ShExDocParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#rdfLiteral.
    def visitRdfLiteral(self, ctx:ShExDocParser.RdfLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:ShExDocParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#string.
    def visitString(self, ctx:ShExDocParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#iri.
    def visitIri(self, ctx:ShExDocParser.IriContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#prefixedName.
    def visitPrefixedName(self, ctx:ShExDocParser.PrefixedNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#blankNode.
    def visitBlankNode(self, ctx:ShExDocParser.BlankNodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#codeDecl.
    def visitCodeDecl(self, ctx:ShExDocParser.CodeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#productionName.
    def visitProductionName(self, ctx:ShExDocParser.ProductionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#startActions.
    def visitStartActions(self, ctx:ShExDocParser.StartActionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#semanticActions.
    def visitSemanticActions(self, ctx:ShExDocParser.SemanticActionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#rdfType.
    def visitRdfType(self, ctx:ShExDocParser.RdfTypeContext):
        return self.visitChildren(ctx)



del ShExDocParser