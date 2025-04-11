# Generated from PLC_Grammar.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,187,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        4,0,42,8,0,11,0,12,0,43,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,2,1,2,5,2,68,8,2,10,
        2,12,2,71,9,2,1,3,1,3,1,3,1,3,5,3,77,8,3,10,3,12,3,80,9,3,1,4,1,
        4,1,4,1,4,5,4,86,8,4,10,4,12,4,89,9,4,1,5,1,5,5,5,93,8,5,10,5,12,
        5,96,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,107,8,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,3,9,120,8,9,1,10,1,10,1,10,5,
        10,125,8,10,10,10,12,10,128,9,10,1,11,1,11,1,11,5,11,133,8,11,10,
        11,12,11,136,9,11,1,12,1,12,1,12,5,12,141,8,12,10,12,12,12,144,9,
        12,1,13,1,13,1,13,5,13,149,8,13,10,13,12,13,152,9,13,1,14,1,14,1,
        14,5,14,157,8,14,10,14,12,14,160,9,14,1,15,1,15,1,15,5,15,165,8,
        15,10,15,12,15,168,9,15,1,16,3,16,171,8,16,1,16,1,16,1,17,1,17,1,
        17,1,17,1,17,1,17,3,17,181,8,17,1,18,1,18,1,19,1,19,1,19,0,0,20,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,0,7,1,0,15,
        16,1,0,17,18,1,0,19,21,1,0,22,24,2,0,20,20,25,25,1,0,31,34,1,0,26,
        29,189,0,41,1,0,0,0,2,61,1,0,0,0,4,63,1,0,0,0,6,72,1,0,0,0,8,81,
        1,0,0,0,10,90,1,0,0,0,12,99,1,0,0,0,14,108,1,0,0,0,16,114,1,0,0,
        0,18,116,1,0,0,0,20,121,1,0,0,0,22,129,1,0,0,0,24,137,1,0,0,0,26,
        145,1,0,0,0,28,153,1,0,0,0,30,161,1,0,0,0,32,170,1,0,0,0,34,180,
        1,0,0,0,36,182,1,0,0,0,38,184,1,0,0,0,40,42,3,2,1,0,41,40,1,0,0,
        0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,1,1,0,0,0,45,62,5,
        1,0,0,46,47,3,4,2,0,47,48,5,1,0,0,48,62,1,0,0,0,49,50,3,16,8,0,50,
        51,5,1,0,0,51,62,1,0,0,0,52,53,3,6,3,0,53,54,5,1,0,0,54,62,1,0,0,
        0,55,56,3,8,4,0,56,57,5,1,0,0,57,62,1,0,0,0,58,62,3,10,5,0,59,62,
        3,12,6,0,60,62,3,14,7,0,61,45,1,0,0,0,61,46,1,0,0,0,61,49,1,0,0,
        0,61,52,1,0,0,0,61,55,1,0,0,0,61,58,1,0,0,0,61,59,1,0,0,0,61,60,
        1,0,0,0,62,3,1,0,0,0,63,64,3,38,19,0,64,69,5,30,0,0,65,66,5,2,0,
        0,66,68,5,30,0,0,67,65,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,
        1,0,0,0,70,5,1,0,0,0,71,69,1,0,0,0,72,73,5,3,0,0,73,78,5,30,0,0,
        74,75,5,2,0,0,75,77,5,30,0,0,76,74,1,0,0,0,77,80,1,0,0,0,78,76,1,
        0,0,0,78,79,1,0,0,0,79,7,1,0,0,0,80,78,1,0,0,0,81,82,5,4,0,0,82,
        87,3,16,8,0,83,84,5,2,0,0,84,86,3,16,8,0,85,83,1,0,0,0,86,89,1,0,
        0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,9,1,0,0,0,89,87,1,0,0,0,90,94,
        5,5,0,0,91,93,3,2,1,0,92,91,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,
        94,95,1,0,0,0,95,97,1,0,0,0,96,94,1,0,0,0,97,98,5,6,0,0,98,11,1,
        0,0,0,99,100,5,7,0,0,100,101,5,8,0,0,101,102,3,16,8,0,102,103,5,
        9,0,0,103,106,3,2,1,0,104,105,5,10,0,0,105,107,3,2,1,0,106,104,1,
        0,0,0,106,107,1,0,0,0,107,13,1,0,0,0,108,109,5,11,0,0,109,110,5,
        8,0,0,110,111,3,16,8,0,111,112,5,9,0,0,112,113,3,2,1,0,113,15,1,
        0,0,0,114,115,3,18,9,0,115,17,1,0,0,0,116,119,3,20,10,0,117,118,
        5,12,0,0,118,120,3,18,9,0,119,117,1,0,0,0,119,120,1,0,0,0,120,19,
        1,0,0,0,121,126,3,22,11,0,122,123,5,13,0,0,123,125,3,22,11,0,124,
        122,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,127,1,0,0,0,127,
        21,1,0,0,0,128,126,1,0,0,0,129,134,3,24,12,0,130,131,5,14,0,0,131,
        133,3,24,12,0,132,130,1,0,0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,
        135,1,0,0,0,135,23,1,0,0,0,136,134,1,0,0,0,137,142,3,26,13,0,138,
        139,7,0,0,0,139,141,3,26,13,0,140,138,1,0,0,0,141,144,1,0,0,0,142,
        140,1,0,0,0,142,143,1,0,0,0,143,25,1,0,0,0,144,142,1,0,0,0,145,150,
        3,28,14,0,146,147,7,1,0,0,147,149,3,28,14,0,148,146,1,0,0,0,149,
        152,1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,27,1,0,0,0,152,150,
        1,0,0,0,153,158,3,30,15,0,154,155,7,2,0,0,155,157,3,30,15,0,156,
        154,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,1,0,0,0,159,
        29,1,0,0,0,160,158,1,0,0,0,161,166,3,32,16,0,162,163,7,3,0,0,163,
        165,3,32,16,0,164,162,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,
        167,1,0,0,0,167,31,1,0,0,0,168,166,1,0,0,0,169,171,7,4,0,0,170,169,
        1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,173,3,34,17,0,173,33,
        1,0,0,0,174,175,5,8,0,0,175,176,3,16,8,0,176,177,5,9,0,0,177,181,
        1,0,0,0,178,181,3,36,18,0,179,181,5,30,0,0,180,174,1,0,0,0,180,178,
        1,0,0,0,180,179,1,0,0,0,181,35,1,0,0,0,182,183,7,5,0,0,183,37,1,
        0,0,0,184,185,7,6,0,0,185,39,1,0,0,0,16,43,61,69,78,87,94,106,119,
        126,134,142,150,158,166,170,180
    ]

class PLC_GrammarParser ( Parser ):

    grammarFileName = "PLC_Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'read'", "'write'", "'{'", 
                     "'}'", "'if'", "'('", "')'", "'else'", "'while'", "'='", 
                     "'||'", "'&&'", "'=='", "'!='", "'<'", "'>'", "'+'", 
                     "'-'", "'.'", "'*'", "'/'", "'%'", "'!'", "'int'", 
                     "'float'", "'bool'", "'string'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "FLOAT", "BOOL", 
                      "STRING", "NEWLINE", "WS", "COMMENT" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_read = 3
    RULE_write = 4
    RULE_block = 5
    RULE_ifCondition = 6
    RULE_whileCondition = 7
    RULE_expression = 8
    RULE_assignment = 9
    RULE_or = 10
    RULE_and = 11
    RULE_equality = 12
    RULE_relational = 13
    RULE_additive = 14
    RULE_multiplicative = 15
    RULE_unary = 16
    RULE_primary = 17
    RULE_literal = 18
    RULE_type = 19

    ruleNames =  [ "prog", "statement", "declaration", "read", "write", 
                   "block", "ifCondition", "whileCondition", "expression", 
                   "assignment", "or", "and", "equality", "relational", 
                   "additive", "multiplicative", "unary", "primary", "literal", 
                   "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    ID=30
    INT=31
    FLOAT=32
    BOOL=33
    STRING=34
    NEWLINE=35
    WS=36
    COMMENT=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = PLC_GrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.statement()
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 34327235002) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(PLC_GrammarParser.DeclarationContext,0)


        def expression(self):
            return self.getTypedRuleContext(PLC_GrammarParser.ExpressionContext,0)


        def read(self):
            return self.getTypedRuleContext(PLC_GrammarParser.ReadContext,0)


        def write(self):
            return self.getTypedRuleContext(PLC_GrammarParser.WriteContext,0)


        def block(self):
            return self.getTypedRuleContext(PLC_GrammarParser.BlockContext,0)


        def ifCondition(self):
            return self.getTypedRuleContext(PLC_GrammarParser.IfConditionContext,0)


        def whileCondition(self):
            return self.getTypedRuleContext(PLC_GrammarParser.WhileConditionContext,0)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = PLC_GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(PLC_GrammarParser.T__0)
                pass
            elif token in [26, 27, 28, 29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.declaration()
                self.state = 47
                self.match(PLC_GrammarParser.T__0)
                pass
            elif token in [8, 20, 25, 30, 31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.expression()
                self.state = 50
                self.match(PLC_GrammarParser.T__0)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.read()
                self.state = 53
                self.match(PLC_GrammarParser.T__0)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 55
                self.write()
                self.state = 56
                self.match(PLC_GrammarParser.T__0)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 58
                self.block()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 7)
                self.state = 59
                self.ifCondition()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 8)
                self.state = 60
                self.whileCondition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(PLC_GrammarParser.TypeContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PLC_GrammarParser.ID)
            else:
                return self.getToken(PLC_GrammarParser.ID, i)

        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = PLC_GrammarParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.type_()
            self.state = 64
            self.match(PLC_GrammarParser.ID)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 65
                self.match(PLC_GrammarParser.T__1)
                self.state = 66
                self.match(PLC_GrammarParser.ID)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(PLC_GrammarParser.ID)
            else:
                return self.getToken(PLC_GrammarParser.ID, i)

        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_read

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRead" ):
                listener.enterRead(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRead" ):
                listener.exitRead(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRead" ):
                return visitor.visitRead(self)
            else:
                return visitor.visitChildren(self)




    def read(self):

        localctx = PLC_GrammarParser.ReadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_read)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(PLC_GrammarParser.T__2)
            self.state = 73
            self.match(PLC_GrammarParser.ID)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 74
                self.match(PLC_GrammarParser.T__1)
                self.state = 75
                self.match(PLC_GrammarParser.ID)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_write

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite" ):
                listener.enterWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite" ):
                listener.exitWrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = PLC_GrammarParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_write)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(PLC_GrammarParser.T__3)
            self.state = 82
            self.expression()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 83
                self.match(PLC_GrammarParser.T__1)
                self.state = 84
                self.expression()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = PLC_GrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(PLC_GrammarParser.T__4)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34327235002) != 0):
                self.state = 91
                self.statement()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self.match(PLC_GrammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PLC_GrammarParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_ifCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfCondition" ):
                listener.enterIfCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfCondition" ):
                listener.exitIfCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfCondition" ):
                return visitor.visitIfCondition(self)
            else:
                return visitor.visitChildren(self)




    def ifCondition(self):

        localctx = PLC_GrammarParser.IfConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(PLC_GrammarParser.T__6)
            self.state = 100
            self.match(PLC_GrammarParser.T__7)
            self.state = 101
            self.expression()
            self.state = 102
            self.match(PLC_GrammarParser.T__8)
            self.state = 103
            self.statement()
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 104
                self.match(PLC_GrammarParser.T__9)
                self.state = 105
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PLC_GrammarParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(PLC_GrammarParser.StatementContext,0)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_whileCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileCondition" ):
                listener.enterWhileCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileCondition" ):
                listener.exitWhileCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileCondition" ):
                return visitor.visitWhileCondition(self)
            else:
                return visitor.visitChildren(self)




    def whileCondition(self):

        localctx = PLC_GrammarParser.WhileConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_whileCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(PLC_GrammarParser.T__10)
            self.state = 109
            self.match(PLC_GrammarParser.T__7)
            self.state = 110
            self.expression()
            self.state = 111
            self.match(PLC_GrammarParser.T__8)
            self.state = 112
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(PLC_GrammarParser.AssignmentContext,0)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = PLC_GrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_(self):
            return self.getTypedRuleContext(PLC_GrammarParser.OrContext,0)


        def assignment(self):
            return self.getTypedRuleContext(PLC_GrammarParser.AssignmentContext,0)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = PLC_GrammarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.or_()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 117
                self.match(PLC_GrammarParser.T__11)
                self.state = 118
                self.assignment()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def and_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.AndContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.AndContext,i)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_or

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr" ):
                listener.enterOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr" ):
                listener.exitOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)




    def or_(self):

        localctx = PLC_GrammarParser.OrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_or)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.and_()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 122
                self.match(PLC_GrammarParser.T__12)
                self.state = 123
                self.and_()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.EqualityContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.EqualityContext,i)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_and

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnd" ):
                listener.enterAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnd" ):
                listener.exitAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)




    def and_(self):

        localctx = PLC_GrammarParser.AndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_and)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.equality()
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 130
                self.match(PLC_GrammarParser.T__13)
                self.state = 131
                self.equality()
                self.state = 136
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.RelationalContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.RelationalContext,i)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_equality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)




    def equality(self):

        localctx = PLC_GrammarParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.relational()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==16:
                self.state = 138
                _la = self._input.LA(1)
                if not(_la==15 or _la==16):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 139
                self.relational()
                self.state = 144
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.AdditiveContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.AdditiveContext,i)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_relational

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational" ):
                listener.enterRelational(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational" ):
                listener.exitRelational(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = PLC_GrammarParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.additive()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 146
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 147
                self.additive()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.MultiplicativeContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.MultiplicativeContext,i)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_additive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive" ):
                listener.enterAdditive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive" ):
                listener.exitAdditive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive" ):
                return visitor.visitAdditive(self)
            else:
                return visitor.visitChildren(self)




    def additive(self):

        localctx = PLC_GrammarParser.AdditiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.multiplicative()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0):
                self.state = 154
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 155
                self.multiplicative()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.UnaryContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.UnaryContext,i)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_multiplicative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative" ):
                listener.enterMultiplicative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative" ):
                listener.exitMultiplicative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative" ):
                return visitor.visitMultiplicative(self)
            else:
                return visitor.visitChildren(self)




    def multiplicative(self):

        localctx = PLC_GrammarParser.MultiplicativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.unary()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0):
                self.state = 162
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 163
                self.unary()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(PLC_GrammarParser.PrimaryContext,0)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = PLC_GrammarParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20 or _la==25:
                self.state = 169
                _la = self._input.LA(1)
                if not(_la==20 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 172
            self.primary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(PLC_GrammarParser.ExpressionContext,0)


        def literal(self):
            return self.getTypedRuleContext(PLC_GrammarParser.LiteralContext,0)


        def ID(self):
            return self.getToken(PLC_GrammarParser.ID, 0)

        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = PLC_GrammarParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primary)
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.match(PLC_GrammarParser.T__7)
                self.state = 175
                self.expression()
                self.state = 176
                self.match(PLC_GrammarParser.T__8)
                pass
            elif token in [31, 32, 33, 34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.literal()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.match(PLC_GrammarParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PLC_GrammarParser.INT, 0)

        def FLOAT(self):
            return self.getToken(PLC_GrammarParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(PLC_GrammarParser.BOOL, 0)

        def STRING(self):
            return self.getToken(PLC_GrammarParser.STRING, 0)

        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = PLC_GrammarParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32212254720) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = PLC_GrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





