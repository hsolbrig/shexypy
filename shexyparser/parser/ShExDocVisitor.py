# Generated from java-escape by ANTLR 4.5
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by ShExDocParser.

class ShExDocVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ShExDocParser#shExDoc.
    def visitShExDoc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#statement.
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#directive.
    def visitDirective(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassDefinition.
    def visitValueClassDefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassExpr.
    def visitValueClassExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassLabel.
    def visitValueClassLabel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#baseDecl.
    def visitBaseDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#prefixDecl.
    def visitPrefixDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#start.
    def visitStart(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#shape.
    def visitShape(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#shapeDefinition.
    def visitShapeDefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#includeSet.
    def visitIncludeSet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#inclPropertySet.
    def visitInclPropertySet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#someOfShape.
    def visitSomeOfShape(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#groupShape.
    def visitGroupShape(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#unaryShape.
    def visitUnaryShape(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#include.
    def visitInclude(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#shapeLabel.
    def visitShapeLabel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#tripleConstraint.
    def visitTripleConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#senseFlags.
    def visitSenseFlags(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#predicate.
    def visitPredicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassOrRef.
    def visitValueClassOrRef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassLiteral.
    def visitValueClassLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassNonLiteral.
    def visitValueClassNonLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassDatatype.
    def visitValueClassDatatype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassGroup.
    def visitValueClassGroup(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassValueSet.
    def visitValueClassValueSet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueClassAny.
    def visitValueClassAny(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#groupShapeConstr.
    def visitGroupShapeConstr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#shapeOrRef.
    def visitShapeOrRef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#xsFacet.
    def visitXsFacet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#stringFacet.
    def visitStringFacet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#stringLength.
    def visitStringLength(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#numericFacet.
    def visitNumericFacet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#numericRange.
    def visitNumericRange(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#numericLength.
    def visitNumericLength(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#datatype.
    def visitDatatype(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#annotation.
    def visitAnnotation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#cardinality.
    def visitCardinality(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#repeatRange.
    def visitRepeatRange(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#valueSet.
    def visitValueSet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#value.
    def visitValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#iriRange.
    def visitIriRange(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#exclusion.
    def visitExclusion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#literal.
    def visitLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#numericLiteral.
    def visitNumericLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#rdfLiteral.
    def visitRdfLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#string.
    def visitString(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#iri.
    def visitIri(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#prefixedName.
    def visitPrefixedName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#blankNode.
    def visitBlankNode(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#codeDecl.
    def visitCodeDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#codeLabel.
    def visitCodeLabel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#startActions.
    def visitStartActions(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ShExDocParser#semanticActions.
    def visitSemanticActions(self, ctx):
        return self.visitChildren(ctx)


