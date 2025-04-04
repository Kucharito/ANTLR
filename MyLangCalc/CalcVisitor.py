# Generated from Calc.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete generic visitor for a parse tree produced by CalcParser.

class CalcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalcParser#prog.
    def visitProg(self, ctx:CalcParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#assign.
    def visitAssign(self, ctx:CalcParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#exprStatement.
    def visitExprStatement(self, ctx:CalcParser.ExprStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#parens.
    def visitParens(self, ctx:CalcParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#MulDiv.
    def visitMulDiv(self, ctx:CalcParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#AddSub.
    def visitAddSub(self, ctx:CalcParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#var.
    def visitVar(self, ctx:CalcParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalcParser#int.
    def visitInt(self, ctx:CalcParser.IntContext):
        return self.visitChildren(ctx)



del CalcParser