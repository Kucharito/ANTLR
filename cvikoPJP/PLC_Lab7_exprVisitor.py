# Generated from PLC_Lab7_expr.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .PLC_Lab7_exprParser import PLC_Lab7_exprParser
else:
    from PLC_Lab7_exprParser import PLC_Lab7_exprParser

# This class defines a complete generic visitor for a parse tree produced by PLC_Lab7_exprParser.

class PLC_Lab7_exprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PLC_Lab7_exprParser#prog.
    def visitProg(self, ctx:PLC_Lab7_exprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Lab7_exprParser#stat.
    def visitStat(self, ctx:PLC_Lab7_exprParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PLC_Lab7_exprParser#expr.
    def visitExpr(self, ctx:PLC_Lab7_exprParser.ExprContext):
        return self.visitChildren(ctx)



del PLC_Lab7_exprParser