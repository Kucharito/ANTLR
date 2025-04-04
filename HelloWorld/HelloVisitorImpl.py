from HelloVisitor import HelloVisitor
from HelloParser import HelloParser

class HelloVisitorImpl(HelloVisitor):
    def visitR(self, ctx: HelloParser.RContext):
        name = ctx.ID().getText()
        print(f"Ahoj, {name}!")
