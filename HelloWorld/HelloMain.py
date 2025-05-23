import sys
from antlr4 import *
from HelloLexer import HelloLexer
from HelloParser import HelloParser
from HelloVisitorImpl import HelloVisitorImpl

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = HelloLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.r()
    visitor=HelloVisitorImpl()
    visitor.visit(tree)
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)