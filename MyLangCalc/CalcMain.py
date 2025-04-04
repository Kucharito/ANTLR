import sys
from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from CalcVisitorImpl import CalcVisitorImpl

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CalcLexer(input_stream)
    stream= CommonTokenStream(lexer)
    parser= CalcParser(stream)
    tree=parser.prog()
    
    visitor=CalcVisitorImpl()
    result = visitor.visit(tree)
    print("Výsledok",result)

if __name__ == '__main__':
    main(sys.argv)