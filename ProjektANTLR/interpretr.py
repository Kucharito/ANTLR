from antlr4 import *
from PLC_GrammarLexer import PLC_GrammarLexer
from PLC_GrammarParser import PLC_GrammarParser
from TypeCheckerVisitor import TypeCheckerVisitor
from CodeGeneratorVisitor import CodeGeneratorVisitor
from Interpreter import Interpreter
import sys

def is_stack_code(code: str) -> bool:
    return any(line.strip().upper().startswith(("PUSH", "LOAD", "SAVE", "ADD", "SUB", "MOD", "PRINT")) for line in code.splitlines())

def run_code(input_code):
    if is_stack_code(input_code):
        print("▶ Spúšťam priamo stackový program")
        with open("generated_code.txt", "w", encoding="utf-8") as f:
            f.write(input_code.strip())

        interpreter = Interpreter()
        interpreter.execute("generated_code.txt")
        return

    input_stream = InputStream(input_code + "\n")
    lexer = PLC_GrammarLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = PLC_GrammarParser(tokens)

    tree = parser.prog()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Chyba: Syntaktická chyba.")
        return

    print("Syntax OK")

    type_checker = TypeCheckerVisitor()
    errors = type_checker.visit(tree)
    if errors:
        for err in errors:
            print("Error", err)
        return

    print("Typová kontrola OK")

    code_gen = CodeGeneratorVisitor()
    instructions = code_gen.visit(tree)

    with open("generated_code.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(instructions))

    print("Generovanie kódu OK")

    print("Spúšťam program:")
    interpreter = Interpreter()
    print("\n".join(instructions))
    interpreter.execute("generated_code.txt")

if __name__ == "__main__":
    with open("input.txt", "r", encoding="utf-8") as f:
        full_code = f.read()

    run_code(full_code)
