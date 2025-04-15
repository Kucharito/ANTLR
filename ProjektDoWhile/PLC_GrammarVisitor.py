# Generated from PLC_Grammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .PLC_GrammarParser import PLC_GrammarParser
else:
    from PLC_GrammarParser import PLC_GrammarParser

# This class defines a complete generic visitor for a parse tree produced by PLC_GrammarParser.

class PLC_GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLC_GrammarParser#prog.
    def visitProg(self, ctx:PLC_GrammarParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#statement.
    def visitStatement(self, ctx:PLC_GrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#declaration.
    def visitDeclaration(self, ctx:PLC_GrammarParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#read.
    def visitRead(self, ctx:PLC_GrammarParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#write.
    def visitWrite(self, ctx:PLC_GrammarParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#block.
    def visitBlock(self, ctx:PLC_GrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#ifCondition.
    def visitIfCondition(self, ctx:PLC_GrammarParser.IfConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#whileCondition.
    def visitWhileCondition(self, ctx:PLC_GrammarParser.WhileConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#doWhileCondition.
    def visitDoWhileCondition(self, ctx:PLC_GrammarParser.DoWhileConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#expression.
    def visitExpression(self, ctx:PLC_GrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#assignment.
    def visitAssignment(self, ctx:PLC_GrammarParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#or.
    def visitOr(self, ctx:PLC_GrammarParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#and.
    def visitAnd(self, ctx:PLC_GrammarParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#equality.
    def visitEquality(self, ctx:PLC_GrammarParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#relational.
    def visitRelational(self, ctx:PLC_GrammarParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#additive.
    def visitAdditive(self, ctx:PLC_GrammarParser.AdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#multiplicative.
    def visitMultiplicative(self, ctx:PLC_GrammarParser.MultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#unary.
    def visitUnary(self, ctx:PLC_GrammarParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#primary.
    def visitPrimary(self, ctx:PLC_GrammarParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#literal.
    def visitLiteral(self, ctx:PLC_GrammarParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_GrammarParser#type.
    def visitType(self, ctx:PLC_GrammarParser.TypeContext):
        return self.visitChildren(ctx)



del PLC_GrammarParser