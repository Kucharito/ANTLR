# Generated from PLC_Grammar.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .PLC_GrammarParser import PLC_GrammarParser
else:
    from PLC_GrammarParser import PLC_GrammarParser

# This class defines a complete listener for a parse tree produced by PLC_GrammarParser.
class PLC_GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by PLC_GrammarParser#prog.
    def enterProg(self, ctx:PLC_GrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#prog.
    def exitProg(self, ctx:PLC_GrammarParser.ProgContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#statement.
    def enterStatement(self, ctx:PLC_GrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#statement.
    def exitStatement(self, ctx:PLC_GrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#declaration.
    def enterDeclaration(self, ctx:PLC_GrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#declaration.
    def exitDeclaration(self, ctx:PLC_GrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#read.
    def enterRead(self, ctx:PLC_GrammarParser.ReadContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#read.
    def exitRead(self, ctx:PLC_GrammarParser.ReadContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#write.
    def enterWrite(self, ctx:PLC_GrammarParser.WriteContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#write.
    def exitWrite(self, ctx:PLC_GrammarParser.WriteContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#block.
    def enterBlock(self, ctx:PLC_GrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#block.
    def exitBlock(self, ctx:PLC_GrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#ifCondition.
    def enterIfCondition(self, ctx:PLC_GrammarParser.IfConditionContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#ifCondition.
    def exitIfCondition(self, ctx:PLC_GrammarParser.IfConditionContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#whileCondition.
    def enterWhileCondition(self, ctx:PLC_GrammarParser.WhileConditionContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#whileCondition.
    def exitWhileCondition(self, ctx:PLC_GrammarParser.WhileConditionContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#expression.
    def enterExpression(self, ctx:PLC_GrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#expression.
    def exitExpression(self, ctx:PLC_GrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#assignment.
    def enterAssignment(self, ctx:PLC_GrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#assignment.
    def exitAssignment(self, ctx:PLC_GrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#or.
    def enterOr(self, ctx:PLC_GrammarParser.OrContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#or.
    def exitOr(self, ctx:PLC_GrammarParser.OrContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#and.
    def enterAnd(self, ctx:PLC_GrammarParser.AndContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#and.
    def exitAnd(self, ctx:PLC_GrammarParser.AndContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#equality.
    def enterEquality(self, ctx:PLC_GrammarParser.EqualityContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#equality.
    def exitEquality(self, ctx:PLC_GrammarParser.EqualityContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#relational.
    def enterRelational(self, ctx:PLC_GrammarParser.RelationalContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#relational.
    def exitRelational(self, ctx:PLC_GrammarParser.RelationalContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#additive.
    def enterAdditive(self, ctx:PLC_GrammarParser.AdditiveContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#additive.
    def exitAdditive(self, ctx:PLC_GrammarParser.AdditiveContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#multiplicative.
    def enterMultiplicative(self, ctx:PLC_GrammarParser.MultiplicativeContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#multiplicative.
    def exitMultiplicative(self, ctx:PLC_GrammarParser.MultiplicativeContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#unary.
    def enterUnary(self, ctx:PLC_GrammarParser.UnaryContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#unary.
    def exitUnary(self, ctx:PLC_GrammarParser.UnaryContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#primary.
    def enterPrimary(self, ctx:PLC_GrammarParser.PrimaryContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#primary.
    def exitPrimary(self, ctx:PLC_GrammarParser.PrimaryContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#literal.
    def enterLiteral(self, ctx:PLC_GrammarParser.LiteralContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#literal.
    def exitLiteral(self, ctx:PLC_GrammarParser.LiteralContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#type.
    def enterType(self, ctx:PLC_GrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#type.
    def exitType(self, ctx:PLC_GrammarParser.TypeContext):
        pass



del PLC_GrammarParser