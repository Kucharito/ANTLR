from antlr4 import *
from PLC_GrammarLexer import PLC_GrammarLexer
from PLC_GrammarParser import PLC_GrammarParser
from TypeCheckerVisitor import TypeCheckerVisitor
import sys


def main():
    # Skontrolujte, či bol zadaný vstupný súbor ako argument
    if len(sys.argv) < 2:
        print("Použitie: python interpreter.py <vstupný_súbor>")
        sys.exit(1)

    # Načítanie vstupu zo súboru
    input_file = sys.argv[1]
    try:
        input_stream = FileStream(input_file, encoding="utf-8")
    except FileNotFoundError:
        print(f"Chyba: Súbor '{input_file}' neexistuje.")
        sys.exit(1)

    # Inicializácia lexeru, parsera a návštevníka
    lexer = PLC_GrammarLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = PLC_GrammarParser(tokens)
    visitor = TypeCheckerVisitor()

    # Skontrolujte syntax
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Chyba v syntaxi!")
        sys.exit(1)

    print("Syntakticky správne!")

    # Vytvorenie syntaktického stromu a jeho návšteva
    tree = parser.prog()
    result = visitor.visit(tree)

    # Výpis výsledkov alebo chýb
    if visitor.errors:
        print("Typové chyby:")
        for error in visitor.errors:
            print(error)
    else:
        print("Typovo správne!")


if __name__ == "__main__":
    main()
