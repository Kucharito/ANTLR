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
        4,1,40,203,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,4,0,44,8,0,11,0,12,0,45,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,67,8,1,1,2,1,2,1,
        2,1,2,5,2,73,8,2,10,2,12,2,76,9,2,1,2,1,2,3,2,80,8,2,1,3,1,3,1,3,
        1,3,5,3,86,8,3,10,3,12,3,89,9,3,1,4,1,4,1,4,1,4,5,4,95,8,4,10,4,
        12,4,98,9,4,1,5,1,5,5,5,102,8,5,10,5,12,5,105,9,5,1,5,1,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,3,6,116,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,
        8,1,8,4,8,127,8,8,11,8,12,8,128,1,9,1,9,1,10,1,10,1,10,3,10,136,
        8,10,1,11,1,11,1,11,5,11,141,8,11,10,11,12,11,144,9,11,1,12,1,12,
        1,12,5,12,149,8,12,10,12,12,12,152,9,12,1,13,1,13,1,13,5,13,157,
        8,13,10,13,12,13,160,9,13,1,14,1,14,1,14,5,14,165,8,14,10,14,12,
        14,168,9,14,1,15,1,15,1,15,5,15,173,8,15,10,15,12,15,176,9,15,1,
        16,1,16,1,16,5,16,181,8,16,10,16,12,16,184,9,16,1,17,3,17,187,8,
        17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,197,8,18,1,19,1,
        19,1,20,1,20,1,20,0,0,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,0,7,1,0,16,17,1,0,18,19,1,0,20,22,1,0,23,25,2,
        0,21,21,26,26,1,0,34,37,1,0,27,31,207,0,43,1,0,0,0,2,66,1,0,0,0,
        4,68,1,0,0,0,6,81,1,0,0,0,8,90,1,0,0,0,10,99,1,0,0,0,12,108,1,0,
        0,0,14,117,1,0,0,0,16,123,1,0,0,0,18,130,1,0,0,0,20,132,1,0,0,0,
        22,137,1,0,0,0,24,145,1,0,0,0,26,153,1,0,0,0,28,161,1,0,0,0,30,169,
        1,0,0,0,32,177,1,0,0,0,34,186,1,0,0,0,36,196,1,0,0,0,38,198,1,0,
        0,0,40,200,1,0,0,0,42,44,3,2,1,0,43,42,1,0,0,0,44,45,1,0,0,0,45,
        43,1,0,0,0,45,46,1,0,0,0,46,1,1,0,0,0,47,67,5,1,0,0,48,49,3,4,2,
        0,49,50,5,1,0,0,50,67,1,0,0,0,51,52,3,18,9,0,52,53,5,1,0,0,53,67,
        1,0,0,0,54,55,3,6,3,0,55,56,5,1,0,0,56,67,1,0,0,0,57,58,3,8,4,0,
        58,59,5,1,0,0,59,67,1,0,0,0,60,67,3,10,5,0,61,67,3,12,6,0,62,67,
        3,14,7,0,63,64,3,16,8,0,64,65,5,1,0,0,65,67,1,0,0,0,66,47,1,0,0,
        0,66,48,1,0,0,0,66,51,1,0,0,0,66,54,1,0,0,0,66,57,1,0,0,0,66,60,
        1,0,0,0,66,61,1,0,0,0,66,62,1,0,0,0,66,63,1,0,0,0,67,3,1,0,0,0,68,
        69,3,40,20,0,69,74,5,33,0,0,70,71,5,2,0,0,71,73,5,33,0,0,72,70,1,
        0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,79,1,0,0,0,76,
        74,1,0,0,0,77,78,5,3,0,0,78,80,3,18,9,0,79,77,1,0,0,0,79,80,1,0,
        0,0,80,5,1,0,0,0,81,82,5,4,0,0,82,87,5,33,0,0,83,84,5,2,0,0,84,86,
        5,33,0,0,85,83,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,
        88,7,1,0,0,0,89,87,1,0,0,0,90,91,5,5,0,0,91,96,3,18,9,0,92,93,5,
        2,0,0,93,95,3,18,9,0,94,92,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,
        97,1,0,0,0,97,9,1,0,0,0,98,96,1,0,0,0,99,103,5,6,0,0,100,102,3,2,
        1,0,101,100,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,
        0,0,104,106,1,0,0,0,105,103,1,0,0,0,106,107,5,7,0,0,107,11,1,0,0,
        0,108,109,5,8,0,0,109,110,5,9,0,0,110,111,3,18,9,0,111,112,5,10,
        0,0,112,115,3,2,1,0,113,114,5,11,0,0,114,116,3,2,1,0,115,113,1,0,
        0,0,115,116,1,0,0,0,116,13,1,0,0,0,117,118,5,12,0,0,118,119,5,9,
        0,0,119,120,3,18,9,0,120,121,5,10,0,0,121,122,3,2,1,0,122,15,1,0,
        0,0,123,126,5,33,0,0,124,125,5,13,0,0,125,127,3,20,10,0,126,124,
        1,0,0,0,127,128,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,17,1,
        0,0,0,130,131,3,20,10,0,131,19,1,0,0,0,132,135,3,22,11,0,133,134,
        5,3,0,0,134,136,3,20,10,0,135,133,1,0,0,0,135,136,1,0,0,0,136,21,
        1,0,0,0,137,142,3,24,12,0,138,139,5,14,0,0,139,141,3,24,12,0,140,
        138,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,
        23,1,0,0,0,144,142,1,0,0,0,145,150,3,26,13,0,146,147,5,15,0,0,147,
        149,3,26,13,0,148,146,1,0,0,0,149,152,1,0,0,0,150,148,1,0,0,0,150,
        151,1,0,0,0,151,25,1,0,0,0,152,150,1,0,0,0,153,158,3,28,14,0,154,
        155,7,0,0,0,155,157,3,28,14,0,156,154,1,0,0,0,157,160,1,0,0,0,158,
        156,1,0,0,0,158,159,1,0,0,0,159,27,1,0,0,0,160,158,1,0,0,0,161,166,
        3,30,15,0,162,163,7,1,0,0,163,165,3,30,15,0,164,162,1,0,0,0,165,
        168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,29,1,0,0,0,168,166,
        1,0,0,0,169,174,3,32,16,0,170,171,7,2,0,0,171,173,3,32,16,0,172,
        170,1,0,0,0,173,176,1,0,0,0,174,172,1,0,0,0,174,175,1,0,0,0,175,
        31,1,0,0,0,176,174,1,0,0,0,177,182,3,34,17,0,178,179,7,3,0,0,179,
        181,3,34,17,0,180,178,1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,182,
        183,1,0,0,0,183,33,1,0,0,0,184,182,1,0,0,0,185,187,7,4,0,0,186,185,
        1,0,0,0,186,187,1,0,0,0,187,188,1,0,0,0,188,189,3,36,18,0,189,35,
        1,0,0,0,190,191,5,9,0,0,191,192,3,18,9,0,192,193,5,10,0,0,193,197,
        1,0,0,0,194,197,3,38,19,0,195,197,5,33,0,0,196,190,1,0,0,0,196,194,
        1,0,0,0,196,195,1,0,0,0,197,37,1,0,0,0,198,199,7,5,0,0,199,39,1,
        0,0,0,200,201,7,6,0,0,201,41,1,0,0,0,18,45,66,74,79,87,96,103,115,
        128,135,142,150,158,166,174,182,186,196
    ]

class PLC_GrammarParser ( Parser ):

    grammarFileName = "PLC_Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'='", "'read'", "'write'", 
                     "'{'", "'}'", "'if'", "'('", "')'", "'else'", "'while'", 
                     "'<<'", "'||'", "'&&'", "'=='", "'!='", "'<'", "'>'", 
                     "'+'", "'-'", "'.'", "'*'", "'/'", "'%'", "'!'", "'int'", 
                     "'float'", "'bool'", "'string'", "'FILE'", "'file'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "FILE", "ID", "INT", "FLOAT", "BOOL", "STRING", "NEWLINE", 
                      "WS", "COMMENT" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_read = 3
    RULE_write = 4
    RULE_block = 5
    RULE_ifCondition = 6
    RULE_whileCondition = 7
    RULE_fileWrite = 8
    RULE_expression = 9
    RULE_assignment = 10
    RULE_or = 11
    RULE_and = 12
    RULE_equality = 13
    RULE_relational = 14
    RULE_additive = 15
    RULE_multiplicative = 16
    RULE_unary = 17
    RULE_primary = 18
    RULE_literal = 19
    RULE_type = 20

    ruleNames =  [ "prog", "statement", "declaration", "read", "write", 
                   "block", "ifCondition", "whileCondition", "fileWrite", 
                   "expression", "assignment", "or", "and", "equality", 
                   "relational", "additive", "multiplicative", "unary", 
                   "primary", "literal", "type" ]

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
    T__29=30
    T__30=31
    FILE=32
    ID=33
    INT=34
    FLOAT=35
    BOOL=36
    STRING=37
    NEWLINE=38
    WS=39
    COMMENT=40

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
            self.state = 43 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 42
                self.statement()
                self.state = 45 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 270517932914) != 0)):
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


        def fileWrite(self):
            return self.getTypedRuleContext(PLC_GrammarParser.FileWriteContext,0)


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
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(PLC_GrammarParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.declaration()
                self.state = 49
                self.match(PLC_GrammarParser.T__0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.expression()
                self.state = 52
                self.match(PLC_GrammarParser.T__0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
                self.read()
                self.state = 55
                self.match(PLC_GrammarParser.T__0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 57
                self.write()
                self.state = 58
                self.match(PLC_GrammarParser.T__0)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 60
                self.block()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 61
                self.ifCondition()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 62
                self.whileCondition()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 63
                self.fileWrite()
                self.state = 64
                self.match(PLC_GrammarParser.T__0)
                pass


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

        def expression(self):
            return self.getTypedRuleContext(PLC_GrammarParser.ExpressionContext,0)


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
            self.state = 68
            self.type_()
            self.state = 69
            self.match(PLC_GrammarParser.ID)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 70
                self.match(PLC_GrammarParser.T__1)
                self.state = 71
                self.match(PLC_GrammarParser.ID)
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 77
                self.match(PLC_GrammarParser.T__2)
                self.state = 78
                self.expression()


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
            self.state = 81
            self.match(PLC_GrammarParser.T__3)
            self.state = 82
            self.match(PLC_GrammarParser.ID)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 83
                self.match(PLC_GrammarParser.T__1)
                self.state = 84
                self.match(PLC_GrammarParser.ID)
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
            self.state = 90
            self.match(PLC_GrammarParser.T__4)
            self.state = 91
            self.expression()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 92
                self.match(PLC_GrammarParser.T__1)
                self.state = 93
                self.expression()
                self.state = 98
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
            self.state = 99
            self.match(PLC_GrammarParser.T__5)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 270517932914) != 0):
                self.state = 100
                self.statement()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
            self.match(PLC_GrammarParser.T__6)
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
            self.state = 108
            self.match(PLC_GrammarParser.T__7)
            self.state = 109
            self.match(PLC_GrammarParser.T__8)
            self.state = 110
            self.expression()
            self.state = 111
            self.match(PLC_GrammarParser.T__9)
            self.state = 112
            self.statement()
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 113
                self.match(PLC_GrammarParser.T__10)
                self.state = 114
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
            self.state = 117
            self.match(PLC_GrammarParser.T__11)
            self.state = 118
            self.match(PLC_GrammarParser.T__8)
            self.state = 119
            self.expression()
            self.state = 120
            self.match(PLC_GrammarParser.T__9)
            self.state = 121
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FileWriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(PLC_GrammarParser.ID, 0)

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.AssignmentContext,i)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_fileWrite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFileWrite" ):
                listener.enterFileWrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFileWrite" ):
                listener.exitFileWrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFileWrite" ):
                return visitor.visitFileWrite(self)
            else:
                return visitor.visitChildren(self)




    def fileWrite(self):

        localctx = PLC_GrammarParser.FileWriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_fileWrite)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(PLC_GrammarParser.ID)
            self.state = 126 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 124
                self.match(PLC_GrammarParser.T__12)
                self.state = 125
                self.assignment()
                self.state = 128 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==13):
                    break

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
        self.enterRule(localctx, 18, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
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
        self.enterRule(localctx, 20, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.or_()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 133
                self.match(PLC_GrammarParser.T__2)
                self.state = 134
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
        self.enterRule(localctx, 22, self.RULE_or)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.and_()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 138
                self.match(PLC_GrammarParser.T__13)
                self.state = 139
                self.and_()
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
        self.enterRule(localctx, 24, self.RULE_and)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.equality()
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 146
                self.match(PLC_GrammarParser.T__14)
                self.state = 147
                self.equality()
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
        self.enterRule(localctx, 26, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.relational()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 154
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 155
                self.relational()
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
        self.enterRule(localctx, 28, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.additive()
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 162
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 163
                self.additive()
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
        self.enterRule(localctx, 30, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.multiplicative()
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0):
                self.state = 170
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 171
                self.multiplicative()
                self.state = 176
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
        self.enterRule(localctx, 32, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.unary()
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0):
                self.state = 178
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 179
                self.unary()
                self.state = 184
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
        self.enterRule(localctx, 34, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21 or _la==26:
                self.state = 185
                _la = self._input.LA(1)
                if not(_la==21 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 188
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
        self.enterRule(localctx, 36, self.RULE_primary)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(PLC_GrammarParser.T__8)
                self.state = 191
                self.expression()
                self.state = 192
                self.match(PLC_GrammarParser.T__9)
                pass
            elif token in [34, 35, 36, 37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.literal()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
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
        self.enterRule(localctx, 38, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 257698037760) != 0)):
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
        self.enterRule(localctx, 40, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4160749568) != 0)):
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





