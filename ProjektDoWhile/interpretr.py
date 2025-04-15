from antlr4 import *
from PLC_GrammarLexer import PLC_GrammarLexer
from PLC_GrammarParser import PLC_GrammarParser
from TypeCheckerVisitor import TypeCheckerVisitor

visitor = TypeCheckerVisitor()

print("PLC REPL – syntax a typová kontrola")

while True:
    try:
        line = input(">> ")
        if not line.strip():
            continue

        input_stream = InputStream(line + "\n")
        lexer = PLC_GrammarLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = PLC_GrammarParser(tokens)

        tree = parser.statement()

        if parser.getNumberOfSyntaxErrors() > 0:
            print("❌ Chyba: Syntaktická chyba.")
            continue

        print("✓ Syntax OK")

        visitor.visit(tree)
        if visitor.errors:
            for err in visitor.errors:
                print("❌", err)
            visitor.errors.clear()
        else:
            print("✓ Typová kontrola OK")

    except KeyboardInterrupt:
        print("\nBye!")
        break
    except Exception as e:
        print("❌ Chyba:", e)
