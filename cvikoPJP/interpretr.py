from antlr4 import *
from PLC_Lab7_exprLexer import PLC_Lab7_exprLexer
from PLC_Lab7_exprParser import PLC_Lab7_exprParser
from EvalVisitor import EvalVisitor

visitor = EvalVisitor()

print("PLC Expr REPL - zadej vyraz nebo priradenie­ (Ctrl+C pro ukoncenie):")
while True:
    try:
        line = input('>> ')
        input_stream = InputStream(line + '\n')  # NEWLINE je souÄŤĂˇst syntaxe!
        lexer = PLC_Lab7_exprLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = PLC_Lab7_exprParser(tokens)
        tree = parser.stat()
        result = visitor.visit(tree)
        if result is not None:
            print(result)
    except KeyboardInterrupt:
        print("\nBye!")
        break
    except Exception as e:
        print("Chyba:", e)