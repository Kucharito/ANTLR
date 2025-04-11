from antlr4 import *
from PLC_Lab7_exprLexer import PLC_Lab7_exprLexer
from PLC_Lab7_exprParser import PLC_Lab7_exprParser
from EvalVisitor import EvalVisitor
from EvalListener import EvalListener

def main():
    input_text = """
a = 3
b = 4
a + b * 2
(1 + 2) * 3
"""
    input_stream = InputStream(input_text)
    lexer = PLC_Lab7_exprLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = PLC_Lab7_exprParser(tokens)

    tree = parser.prog()
    visitor = EvalVisitor()
    results = visitor.visit(tree)

    for r in results:
        print(r)

    listener = EvalListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    for key, value in listener.values.items():
        print(f"{key}: {value}")

if __name__ == '__main__':
    main()