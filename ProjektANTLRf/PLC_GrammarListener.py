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


    # Enter a parse tree produced by PLC_GrammarParser#stat.
    def enterStat(self, ctx:PLC_GrammarParser.StatContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#stat.
    def exitStat(self, ctx:PLC_GrammarParser.StatContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#declaration.
    def enterDeclaration(self, ctx:PLC_GrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#declaration.
    def exitDeclaration(self, ctx:PLC_GrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#expression.
    def enterExpression(self, ctx:PLC_GrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#expression.
    def exitExpression(self, ctx:PLC_GrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#assignement.
    def enterAssignement(self, ctx:PLC_GrammarParser.AssignementContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#assignement.
    def exitAssignement(self, ctx:PLC_GrammarParser.AssignementContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#concatExpression.
    def enterConcatExpression(self, ctx:PLC_GrammarParser.ConcatExpressionContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#concatExpression.
    def exitConcatExpression(self, ctx:PLC_GrammarParser.ConcatExpressionContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#orExpression.
    def enterOrExpression(self, ctx:PLC_GrammarParser.OrExpressionContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#orExpression.
    def exitOrExpression(self, ctx:PLC_GrammarParser.OrExpressionContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#andExpression.
    def enterAndExpression(self, ctx:PLC_GrammarParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#andExpression.
    def exitAndExpression(self, ctx:PLC_GrammarParser.AndExpressionContext):
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


    # Enter a parse tree produced by PLC_GrammarParser#forCondition.
    def enterForCondition(self, ctx:PLC_GrammarParser.ForConditionContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#forCondition.
    def exitForCondition(self, ctx:PLC_GrammarParser.ForConditionContext):
        pass


    # Enter a parse tree produced by PLC_GrammarParser#type.
    def enterType(self, ctx:PLC_GrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by PLC_GrammarParser#type.
    def exitType(self, ctx:PLC_GrammarParser.TypeContext):
        pass



del PLC_GrammarParser