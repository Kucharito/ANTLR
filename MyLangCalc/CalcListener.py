# Generated from Calc.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete listener for a parse tree produced by CalcParser.
class CalcListener(ParseTreeListener):

    # Enter a parse tree produced by CalcParser#prog.
    def enterProg(self, ctx:CalcParser.ProgContext):
        pass

    # Exit a parse tree produced by CalcParser#prog.
    def exitProg(self, ctx:CalcParser.ProgContext):
        pass


    # Enter a parse tree produced by CalcParser#assign.
    def enterAssign(self, ctx:CalcParser.AssignContext):
        pass

    # Exit a parse tree produced by CalcParser#assign.
    def exitAssign(self, ctx:CalcParser.AssignContext):
        pass


    # Enter a parse tree produced by CalcParser#exprStatement.
    def enterExprStatement(self, ctx:CalcParser.ExprStatementContext):
        pass

    # Exit a parse tree produced by CalcParser#exprStatement.
    def exitExprStatement(self, ctx:CalcParser.ExprStatementContext):
        pass


    # Enter a parse tree produced by CalcParser#parens.
    def enterParens(self, ctx:CalcParser.ParensContext):
        pass

    # Exit a parse tree produced by CalcParser#parens.
    def exitParens(self, ctx:CalcParser.ParensContext):
        pass


    # Enter a parse tree produced by CalcParser#MulDiv.
    def enterMulDiv(self, ctx:CalcParser.MulDivContext):
        pass

    # Exit a parse tree produced by CalcParser#MulDiv.
    def exitMulDiv(self, ctx:CalcParser.MulDivContext):
        pass


    # Enter a parse tree produced by CalcParser#AddSub.
    def enterAddSub(self, ctx:CalcParser.AddSubContext):
        pass

    # Exit a parse tree produced by CalcParser#AddSub.
    def exitAddSub(self, ctx:CalcParser.AddSubContext):
        pass


    # Enter a parse tree produced by CalcParser#var.
    def enterVar(self, ctx:CalcParser.VarContext):
        pass

    # Exit a parse tree produced by CalcParser#var.
    def exitVar(self, ctx:CalcParser.VarContext):
        pass


    # Enter a parse tree produced by CalcParser#int.
    def enterInt(self, ctx:CalcParser.IntContext):
        pass

    # Exit a parse tree produced by CalcParser#int.
    def exitInt(self, ctx:CalcParser.IntContext):
        pass



del CalcParser