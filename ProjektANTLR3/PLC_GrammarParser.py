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
        4,1,39,196,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,4,0,44,8,0,11,0,12,0,45,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,65,8,1,1,2,1,2,1,2,1,2,5,
        2,71,8,2,10,2,12,2,74,9,2,1,3,1,3,1,3,1,3,5,3,80,8,3,10,3,12,3,83,
        9,3,1,4,1,4,1,4,1,4,5,4,89,8,4,10,4,12,4,92,9,4,1,5,1,5,5,5,96,8,
        5,10,5,12,5,99,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,110,8,
        6,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,10,1,
        10,1,10,3,10,129,8,10,1,11,1,11,1,11,5,11,134,8,11,10,11,12,11,137,
        9,11,1,12,1,12,1,12,5,12,142,8,12,10,12,12,12,145,9,12,1,13,1,13,
        1,13,5,13,150,8,13,10,13,12,13,153,9,13,1,14,1,14,1,14,5,14,158,
        8,14,10,14,12,14,161,9,14,1,15,1,15,1,15,5,15,166,8,15,10,15,12,
        15,169,9,15,1,16,1,16,1,16,5,16,174,8,16,10,16,12,16,177,9,16,1,
        17,3,17,180,8,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,3,18,190,
        8,18,1,19,1,19,1,20,1,20,1,20,0,0,21,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,0,7,1,0,17,18,1,0,19,20,1,0,21,23,
        1,0,24,26,2,0,22,22,27,27,1,0,33,36,1,0,28,31,198,0,43,1,0,0,0,2,
        64,1,0,0,0,4,66,1,0,0,0,6,75,1,0,0,0,8,84,1,0,0,0,10,93,1,0,0,0,
        12,102,1,0,0,0,14,111,1,0,0,0,16,117,1,0,0,0,18,123,1,0,0,0,20,125,
        1,0,0,0,22,130,1,0,0,0,24,138,1,0,0,0,26,146,1,0,0,0,28,154,1,0,
        0,0,30,162,1,0,0,0,32,170,1,0,0,0,34,179,1,0,0,0,36,189,1,0,0,0,
        38,191,1,0,0,0,40,193,1,0,0,0,42,44,3,2,1,0,43,42,1,0,0,0,44,45,
        1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,1,1,0,0,0,47,65,5,1,0,0,48,
        49,3,4,2,0,49,50,5,1,0,0,50,65,1,0,0,0,51,52,3,18,9,0,52,53,5,1,
        0,0,53,65,1,0,0,0,54,55,3,6,3,0,55,56,5,1,0,0,56,65,1,0,0,0,57,58,
        3,8,4,0,58,59,5,1,0,0,59,65,1,0,0,0,60,65,3,10,5,0,61,65,3,12,6,
        0,62,65,3,14,7,0,63,65,3,16,8,0,64,47,1,0,0,0,64,48,1,0,0,0,64,51,
        1,0,0,0,64,54,1,0,0,0,64,57,1,0,0,0,64,60,1,0,0,0,64,61,1,0,0,0,
        64,62,1,0,0,0,64,63,1,0,0,0,65,3,1,0,0,0,66,67,3,40,20,0,67,72,5,
        32,0,0,68,69,5,2,0,0,69,71,5,32,0,0,70,68,1,0,0,0,71,74,1,0,0,0,
        72,70,1,0,0,0,72,73,1,0,0,0,73,5,1,0,0,0,74,72,1,0,0,0,75,76,5,3,
        0,0,76,81,5,32,0,0,77,78,5,2,0,0,78,80,5,32,0,0,79,77,1,0,0,0,80,
        83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,7,1,0,0,0,83,81,1,0,0,
        0,84,85,5,4,0,0,85,90,3,18,9,0,86,87,5,2,0,0,87,89,3,18,9,0,88,86,
        1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,9,1,0,0,0,92,
        90,1,0,0,0,93,97,5,5,0,0,94,96,3,2,1,0,95,94,1,0,0,0,96,99,1,0,0,
        0,97,95,1,0,0,0,97,98,1,0,0,0,98,100,1,0,0,0,99,97,1,0,0,0,100,101,
        5,6,0,0,101,11,1,0,0,0,102,103,5,7,0,0,103,104,5,8,0,0,104,105,3,
        18,9,0,105,106,5,9,0,0,106,109,3,2,1,0,107,108,5,10,0,0,108,110,
        3,2,1,0,109,107,1,0,0,0,109,110,1,0,0,0,110,13,1,0,0,0,111,112,5,
        11,0,0,112,113,5,8,0,0,113,114,3,18,9,0,114,115,5,9,0,0,115,116,
        3,2,1,0,116,15,1,0,0,0,117,118,3,18,9,0,118,119,5,12,0,0,119,120,
        3,18,9,0,120,121,5,13,0,0,121,122,3,18,9,0,122,17,1,0,0,0,123,124,
        3,20,10,0,124,19,1,0,0,0,125,128,3,22,11,0,126,127,5,14,0,0,127,
        129,3,20,10,0,128,126,1,0,0,0,128,129,1,0,0,0,129,21,1,0,0,0,130,
        135,3,24,12,0,131,132,5,15,0,0,132,134,3,24,12,0,133,131,1,0,0,0,
        134,137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,23,1,0,0,0,137,
        135,1,0,0,0,138,143,3,26,13,0,139,140,5,16,0,0,140,142,3,26,13,0,
        141,139,1,0,0,0,142,145,1,0,0,0,143,141,1,0,0,0,143,144,1,0,0,0,
        144,25,1,0,0,0,145,143,1,0,0,0,146,151,3,28,14,0,147,148,7,0,0,0,
        148,150,3,28,14,0,149,147,1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,
        0,151,152,1,0,0,0,152,27,1,0,0,0,153,151,1,0,0,0,154,159,3,30,15,
        0,155,156,7,1,0,0,156,158,3,30,15,0,157,155,1,0,0,0,158,161,1,0,
        0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,29,1,0,0,0,161,159,1,0,0,
        0,162,167,3,32,16,0,163,164,7,2,0,0,164,166,3,32,16,0,165,163,1,
        0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,31,1,0,
        0,0,169,167,1,0,0,0,170,175,3,34,17,0,171,172,7,3,0,0,172,174,3,
        34,17,0,173,171,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,
        1,0,0,0,176,33,1,0,0,0,177,175,1,0,0,0,178,180,7,4,0,0,179,178,1,
        0,0,0,179,180,1,0,0,0,180,181,1,0,0,0,181,182,3,36,18,0,182,35,1,
        0,0,0,183,184,5,8,0,0,184,185,3,18,9,0,185,186,5,9,0,0,186,190,1,
        0,0,0,187,190,3,38,19,0,188,190,5,32,0,0,189,183,1,0,0,0,189,187,
        1,0,0,0,189,188,1,0,0,0,190,37,1,0,0,0,191,192,7,5,0,0,192,39,1,
        0,0,0,193,194,7,6,0,0,194,41,1,0,0,0,16,45,64,72,81,90,97,109,128,
        135,143,151,159,167,175,179,189
    ]

class PLC_GrammarParser ( Parser ):

    grammarFileName = "PLC_Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'read'", "'write'", "'{'", 
                     "'}'", "'if'", "'('", "')'", "'else'", "'while'", "'?'", 
                     "':'", "'='", "'||'", "'&&'", "'=='", "'!='", "'<'", 
                     "'>'", "'+'", "'-'", "'.'", "'*'", "'/'", "'%'", "'!'", 
                     "'int'", "'float'", "'bool'", "'string'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "FLOAT", "BOOL", "STRING", "NEWLINE", 
                      "WS", "COMMENT" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_read = 3
    RULE_write = 4
    RULE_block = 5
    RULE_ifCondition = 6
    RULE_whileCondition = 7
    RULE_ternaryOperator = 8
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
                   "block", "ifCondition", "whileCondition", "ternaryOperator", 
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
    ID=32
    INT=33
    FLOAT=34
    BOOL=35
    STRING=36
    NEWLINE=37
    WS=38
    COMMENT=39

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
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 137308932538) != 0)):
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


        def ternaryOperator(self):
            return self.getTypedRuleContext(PLC_GrammarParser.TernaryOperatorContext,0)


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
            self.state = 64
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
                self.ternaryOperator()
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
            self.state = 66
            self.type_()
            self.state = 67
            self.match(PLC_GrammarParser.ID)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 68
                self.match(PLC_GrammarParser.T__1)
                self.state = 69
                self.match(PLC_GrammarParser.ID)
                self.state = 74
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
            self.state = 75
            self.match(PLC_GrammarParser.T__2)
            self.state = 76
            self.match(PLC_GrammarParser.ID)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 77
                self.match(PLC_GrammarParser.T__1)
                self.state = 78
                self.match(PLC_GrammarParser.ID)
                self.state = 83
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
            self.state = 84
            self.match(PLC_GrammarParser.T__3)
            self.state = 85
            self.expression()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 86
                self.match(PLC_GrammarParser.T__1)
                self.state = 87
                self.expression()
                self.state = 92
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
            self.state = 93
            self.match(PLC_GrammarParser.T__4)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137308932538) != 0):
                self.state = 94
                self.statement()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 100
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
            self.state = 102
            self.match(PLC_GrammarParser.T__6)
            self.state = 103
            self.match(PLC_GrammarParser.T__7)
            self.state = 104
            self.expression()
            self.state = 105
            self.match(PLC_GrammarParser.T__8)
            self.state = 106
            self.statement()
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 107
                self.match(PLC_GrammarParser.T__9)
                self.state = 108
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
            self.state = 111
            self.match(PLC_GrammarParser.T__10)
            self.state = 112
            self.match(PLC_GrammarParser.T__7)
            self.state = 113
            self.expression()
            self.state = 114
            self.match(PLC_GrammarParser.T__8)
            self.state = 115
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TernaryOperatorContext(ParserRuleContext):
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
            return PLC_GrammarParser.RULE_ternaryOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTernaryOperator" ):
                listener.enterTernaryOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTernaryOperator" ):
                listener.exitTernaryOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTernaryOperator" ):
                return visitor.visitTernaryOperator(self)
            else:
                return visitor.visitChildren(self)




    def ternaryOperator(self):

        localctx = PLC_GrammarParser.TernaryOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ternaryOperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.expression()
            self.state = 118
            self.match(PLC_GrammarParser.T__11)
            self.state = 119
            self.expression()
            self.state = 120
            self.match(PLC_GrammarParser.T__12)
            self.state = 121
            self.expression()
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
            self.state = 123
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
            self.state = 125
            self.or_()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 126
                self.match(PLC_GrammarParser.T__13)
                self.state = 127
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
            self.state = 130
            self.and_()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15:
                self.state = 131
                self.match(PLC_GrammarParser.T__14)
                self.state = 132
                self.and_()
                self.state = 137
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
            self.state = 138
            self.equality()
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 139
                self.match(PLC_GrammarParser.T__15)
                self.state = 140
                self.equality()
                self.state = 145
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
            self.state = 146
            self.relational()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 147
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 148
                self.relational()
                self.state = 153
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
            self.state = 154
            self.additive()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19 or _la==20:
                self.state = 155
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 156
                self.additive()
                self.state = 161
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
            self.state = 162
            self.multiplicative()
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 163
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 164
                    self.multiplicative() 
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
            self.state = 170
            self.unary()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0):
                self.state = 171
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 117440512) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 172
                self.unary()
                self.state = 177
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
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22 or _la==27:
                self.state = 178
                _la = self._input.LA(1)
                if not(_la==22 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 181
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
            self.state = 189
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(PLC_GrammarParser.T__7)
                self.state = 184
                self.expression()
                self.state = 185
                self.match(PLC_GrammarParser.T__8)
                pass
            elif token in [33, 34, 35, 36]:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.literal()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
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
            self.state = 191
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 128849018880) != 0)):
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
            self.state = 193
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4026531840) != 0)):
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





