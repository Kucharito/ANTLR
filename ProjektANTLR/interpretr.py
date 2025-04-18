from antlr4 import *
from PLC_GrammarLexer import PLC_GrammarLexer
from PLC_GrammarParser import PLC_GrammarParser
from TypeCheckerVisitor import TypeCheckerVisitor
from CodeGeneratorVisitor import CodeGeneratorVisitor
from Interpreter import Interpreter

def run_code(input_code):
    input_stream = InputStream(input_code + "\n")
    lexer = PLC_GrammarLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = PLC_GrammarParser(tokens)

    tree = parser.prog()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("❌ Chyba: Syntaktická chyba.")
        return

    print("✓ Syntax OK")

    # Typová kontrola
    type_checker = TypeCheckerVisitor()
    errors = type_checker.visit(tree)
    if errors:
        for err in errors:
            print("❌", err)
        return

    print("✓ Typová kontrola OK")

    # Generovanie inštrukcií
    code_gen = CodeGeneratorVisitor()
    instructions = code_gen.visit(tree)

    with open("generated_code.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(instructions))

    print("✓ Generovanie kódu OK")

    # Spusti interpreter
    print("▶ Spúšťam program:")
    interpreter = Interpreter()
    print("====== GENERATED CODE ======")
    print("\n".join(instructions))

    interpreter.execute("generated_code.txt")


if __name__ == "__main__":
    # Tu načítaš svoj zdrojový súbor s write, read, atď.
    with open("input.txt", "r", encoding="utf-8") as f:
        full_code = f.read()

    run_code(full_code)
