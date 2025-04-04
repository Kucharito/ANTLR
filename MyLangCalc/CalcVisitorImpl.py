from CalcVisitor import CalcVisitor
from CalcParser import CalcParser

class CalcVisitorImpl(CalcVisitor):
    def __init__(self):
        self.memory = {} 

    def visitProg(self, ctx):
        result = None
        for child in ctx.stat():
            result = self.visit(child)
        return result

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        return value

    def visitExprStatement(self, ctx):
        return self.visit(ctx.expr())

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        return left + right if op == '+' else left - right

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        return left * right if op == '*' else left / right

    def visitInt(self, ctx):
        return int(ctx.getText())

    def visitVar(self, ctx):
        name = ctx.getText()
        return self.memory.get(name, 0)

    def visitParens(self, ctx):
        return self.visit(ctx.expr())
