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
        4,1,38,211,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,68,8,1,1,2,
        1,2,1,2,1,2,5,2,74,8,2,10,2,12,2,77,9,2,1,3,1,3,1,4,1,4,1,4,3,4,
        84,8,4,1,5,1,5,1,5,5,5,89,8,5,10,5,12,5,92,9,5,1,6,1,6,1,6,5,6,97,
        8,6,10,6,12,6,100,9,6,1,7,1,7,1,7,5,7,105,8,7,10,7,12,7,108,9,7,
        1,8,1,8,1,8,5,8,113,8,8,10,8,12,8,116,9,8,1,9,1,9,1,9,5,9,121,8,
        9,10,9,12,9,124,9,9,1,10,1,10,1,10,5,10,129,8,10,10,10,12,10,132,
        9,10,1,11,1,11,1,11,5,11,137,8,11,10,11,12,11,140,9,11,1,12,3,12,
        143,8,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,153,8,13,1,
        14,1,14,1,15,1,15,1,15,1,15,5,15,161,8,15,10,15,12,15,164,9,15,1,
        16,1,16,1,16,1,16,5,16,170,8,16,10,16,12,16,173,9,16,1,17,1,17,5,
        17,177,8,17,10,17,12,17,180,9,17,1,17,1,17,1,18,1,18,1,18,1,18,1,
        18,1,18,1,18,3,18,191,8,18,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,0,0,22,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,0,7,
        1,0,7,8,1,0,9,10,1,0,11,13,1,0,14,16,2,0,12,12,17,17,2,0,32,33,35,
        36,1,0,28,31,213,0,47,1,0,0,0,2,67,1,0,0,0,4,69,1,0,0,0,6,78,1,0,
        0,0,8,80,1,0,0,0,10,85,1,0,0,0,12,93,1,0,0,0,14,101,1,0,0,0,16,109,
        1,0,0,0,18,117,1,0,0,0,20,125,1,0,0,0,22,133,1,0,0,0,24,142,1,0,
        0,0,26,152,1,0,0,0,28,154,1,0,0,0,30,156,1,0,0,0,32,165,1,0,0,0,
        34,174,1,0,0,0,36,183,1,0,0,0,38,192,1,0,0,0,40,198,1,0,0,0,42,208,
        1,0,0,0,44,46,3,2,1,0,45,44,1,0,0,0,46,49,1,0,0,0,47,45,1,0,0,0,
        47,48,1,0,0,0,48,1,1,0,0,0,49,47,1,0,0,0,50,68,5,1,0,0,51,52,3,4,
        2,0,52,53,5,1,0,0,53,68,1,0,0,0,54,55,3,6,3,0,55,56,5,1,0,0,56,68,
        1,0,0,0,57,58,3,30,15,0,58,59,5,1,0,0,59,68,1,0,0,0,60,61,3,32,16,
        0,61,62,5,1,0,0,62,68,1,0,0,0,63,68,3,34,17,0,64,68,3,36,18,0,65,
        68,3,38,19,0,66,68,3,40,20,0,67,50,1,0,0,0,67,51,1,0,0,0,67,54,1,
        0,0,0,67,57,1,0,0,0,67,60,1,0,0,0,67,63,1,0,0,0,67,64,1,0,0,0,67,
        65,1,0,0,0,67,66,1,0,0,0,68,3,1,0,0,0,69,70,3,42,21,0,70,75,5,34,
        0,0,71,72,5,2,0,0,72,74,5,34,0,0,73,71,1,0,0,0,74,77,1,0,0,0,75,
        73,1,0,0,0,75,76,1,0,0,0,76,5,1,0,0,0,77,75,1,0,0,0,78,79,3,8,4,
        0,79,7,1,0,0,0,80,83,3,10,5,0,81,82,5,3,0,0,82,84,3,8,4,0,83,81,
        1,0,0,0,83,84,1,0,0,0,84,9,1,0,0,0,85,90,3,12,6,0,86,87,5,4,0,0,
        87,89,3,12,6,0,88,86,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,
        0,0,0,91,11,1,0,0,0,92,90,1,0,0,0,93,98,3,14,7,0,94,95,5,5,0,0,95,
        97,3,14,7,0,96,94,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,
        0,0,99,13,1,0,0,0,100,98,1,0,0,0,101,106,3,16,8,0,102,103,5,6,0,
        0,103,105,3,16,8,0,104,102,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,
        0,106,107,1,0,0,0,107,15,1,0,0,0,108,106,1,0,0,0,109,114,3,18,9,
        0,110,111,7,0,0,0,111,113,3,18,9,0,112,110,1,0,0,0,113,116,1,0,0,
        0,114,112,1,0,0,0,114,115,1,0,0,0,115,17,1,0,0,0,116,114,1,0,0,0,
        117,122,3,20,10,0,118,119,7,1,0,0,119,121,3,20,10,0,120,118,1,0,
        0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,19,1,0,0,
        0,124,122,1,0,0,0,125,130,3,22,11,0,126,127,7,2,0,0,127,129,3,22,
        11,0,128,126,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,
        0,0,131,21,1,0,0,0,132,130,1,0,0,0,133,138,3,24,12,0,134,135,7,3,
        0,0,135,137,3,24,12,0,136,134,1,0,0,0,137,140,1,0,0,0,138,136,1,
        0,0,0,138,139,1,0,0,0,139,23,1,0,0,0,140,138,1,0,0,0,141,143,7,4,
        0,0,142,141,1,0,0,0,142,143,1,0,0,0,143,144,1,0,0,0,144,145,3,26,
        13,0,145,25,1,0,0,0,146,147,5,18,0,0,147,148,3,6,3,0,148,149,5,19,
        0,0,149,153,1,0,0,0,150,153,5,34,0,0,151,153,3,28,14,0,152,146,1,
        0,0,0,152,150,1,0,0,0,152,151,1,0,0,0,153,27,1,0,0,0,154,155,7,5,
        0,0,155,29,1,0,0,0,156,157,5,20,0,0,157,162,5,34,0,0,158,159,5,2,
        0,0,159,161,5,34,0,0,160,158,1,0,0,0,161,164,1,0,0,0,162,160,1,0,
        0,0,162,163,1,0,0,0,163,31,1,0,0,0,164,162,1,0,0,0,165,166,5,21,
        0,0,166,171,3,6,3,0,167,168,5,2,0,0,168,170,3,6,3,0,169,167,1,0,
        0,0,170,173,1,0,0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,33,1,0,0,
        0,173,171,1,0,0,0,174,178,5,22,0,0,175,177,3,2,1,0,176,175,1,0,0,
        0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,181,1,0,0,
        0,180,178,1,0,0,0,181,182,5,23,0,0,182,35,1,0,0,0,183,184,5,24,0,
        0,184,185,5,18,0,0,185,186,3,6,3,0,186,187,5,19,0,0,187,190,3,2,
        1,0,188,189,5,25,0,0,189,191,3,2,1,0,190,188,1,0,0,0,190,191,1,0,
        0,0,191,37,1,0,0,0,192,193,5,26,0,0,193,194,5,18,0,0,194,195,3,6,
        3,0,195,196,5,19,0,0,196,197,3,2,1,0,197,39,1,0,0,0,198,199,5,27,
        0,0,199,200,5,18,0,0,200,201,3,6,3,0,201,202,5,1,0,0,202,203,3,6,
        3,0,203,204,5,1,0,0,204,205,3,6,3,0,205,206,5,19,0,0,206,207,3,2,
        1,0,207,41,1,0,0,0,208,209,7,6,0,0,209,43,1,0,0,0,17,47,67,75,83,
        90,98,106,114,122,130,138,142,152,162,171,178,190
    ]

class PLC_GrammarParser ( Parser ):

    grammarFileName = "PLC_Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'='", "'<<'", "'||'", "'&&'", 
                     "'=='", "'!='", "'<'", "'>'", "'+'", "'-'", "'.'", 
                     "'*'", "'/'", "'%'", "'!'", "'('", "')'", "'read'", 
                     "'write'", "'{'", "'}'", "'if'", "'else'", "'while'", 
                     "'for'", "'int'", "'float'", "'bool'", "'string'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BOOL", "STRING", "ID", "INT", "FLOAT", "WS", "COMMENT" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_declaration = 2
    RULE_expression = 3
    RULE_assignement = 4
    RULE_concatExpression = 5
    RULE_orExpression = 6
    RULE_andExpression = 7
    RULE_equality = 8
    RULE_relational = 9
    RULE_additive = 10
    RULE_multiplicative = 11
    RULE_unary = 12
    RULE_primary = 13
    RULE_literal = 14
    RULE_read = 15
    RULE_write = 16
    RULE_block = 17
    RULE_ifCondition = 18
    RULE_whileCondition = 19
    RULE_forCondition = 20
    RULE_type = 21

    ruleNames =  [ "prog", "stat", "declaration", "expression", "assignement", 
                   "concatExpression", "orExpression", "andExpression", 
                   "equality", "relational", "additive", "multiplicative", 
                   "unary", "primary", "literal", "read", "write", "block", 
                   "ifCondition", "whileCondition", "forCondition", "type" ]

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
    BOOL=32
    STRING=33
    ID=34
    INT=35
    FLOAT=36
    WS=37
    COMMENT=38

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

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.StatContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.StatContext,i)


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
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137396359170) != 0):
                self.state = 44
                self.stat()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
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


        def forCondition(self):
            return self.getTypedRuleContext(PLC_GrammarParser.ForConditionContext,0)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = PLC_GrammarParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(PLC_GrammarParser.T__0)
                pass
            elif token in [28, 29, 30, 31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.declaration()
                self.state = 52
                self.match(PLC_GrammarParser.T__0)
                pass
            elif token in [12, 17, 18, 32, 33, 34, 35, 36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.expression()
                self.state = 55
                self.match(PLC_GrammarParser.T__0)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.read()
                self.state = 58
                self.match(PLC_GrammarParser.T__0)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.write()
                self.state = 61
                self.match(PLC_GrammarParser.T__0)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 6)
                self.state = 63
                self.block()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 7)
                self.state = 64
                self.ifCondition()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 8)
                self.state = 65
                self.whileCondition()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 9)
                self.state = 66
                self.forCondition()
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
            self.state = 69
            self.type_()
            self.state = 70
            self.match(PLC_GrammarParser.ID)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 71
                self.match(PLC_GrammarParser.T__1)
                self.state = 72
                self.match(PLC_GrammarParser.ID)
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def assignement(self):
            return self.getTypedRuleContext(PLC_GrammarParser.AssignementContext,0)


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
        self.enterRule(localctx, 6, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.assignement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concatExpression(self):
            return self.getTypedRuleContext(PLC_GrammarParser.ConcatExpressionContext,0)


        def assignement(self):
            return self.getTypedRuleContext(PLC_GrammarParser.AssignementContext,0)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_assignement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignement" ):
                listener.enterAssignement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignement" ):
                listener.exitAssignement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignement" ):
                return visitor.visitAssignement(self)
            else:
                return visitor.visitChildren(self)




    def assignement(self):

        localctx = PLC_GrammarParser.AssignementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.concatExpression()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 81
                self.match(PLC_GrammarParser.T__2)
                self.state = 82
                self.assignement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConcatExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.OrExpressionContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.OrExpressionContext,i)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_concatExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatExpression" ):
                listener.enterConcatExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatExpression" ):
                listener.exitConcatExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatExpression" ):
                return visitor.visitConcatExpression(self)
            else:
                return visitor.visitChildren(self)




    def concatExpression(self):

        localctx = PLC_GrammarParser.ConcatExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_concatExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.orExpression()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 86
                self.match(PLC_GrammarParser.T__3)
                self.state = 87
                self.orExpression()
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


    class OrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.AndExpressionContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.AndExpressionContext,i)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_orExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpression" ):
                listener.enterOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpression" ):
                listener.exitOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpression" ):
                return visitor.visitOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def orExpression(self):

        localctx = PLC_GrammarParser.OrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_orExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.andExpression()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 94
                self.match(PLC_GrammarParser.T__4)
                self.state = 95
                self.andExpression()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndExpressionContext(ParserRuleContext):
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
            return PLC_GrammarParser.RULE_andExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpression" ):
                listener.enterAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpression" ):
                listener.exitAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpression" ):
                return visitor.visitAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def andExpression(self):

        localctx = PLC_GrammarParser.AndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_andExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.equality()
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 102
                self.match(PLC_GrammarParser.T__5)
                self.state = 103
                self.equality()
                self.state = 108
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
        self.enterRule(localctx, 16, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.relational()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 110
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 111
                self.relational()
                self.state = 116
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
        self.enterRule(localctx, 18, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.additive()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 118
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 119
                self.additive()
                self.state = 124
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
        self.enterRule(localctx, 20, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.multiplicative()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0):
                self.state = 126
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 127
                self.multiplicative()
                self.state = 132
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
        self.enterRule(localctx, 22, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.unary()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0):
                self.state = 134
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 135
                self.unary()
                self.state = 140
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
        self.enterRule(localctx, 24, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12 or _la==17:
                self.state = 141
                _la = self._input.LA(1)
                if not(_la==12 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 144
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


        def ID(self):
            return self.getToken(PLC_GrammarParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(PLC_GrammarParser.LiteralContext,0)


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
        self.enterRule(localctx, 26, self.RULE_primary)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(PLC_GrammarParser.T__17)
                self.state = 147
                self.expression()
                self.state = 148
                self.match(PLC_GrammarParser.T__18)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(PLC_GrammarParser.ID)
                pass
            elif token in [32, 33, 35, 36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self.literal()
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
        self.enterRule(localctx, 28, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 115964116992) != 0)):
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
        self.enterRule(localctx, 30, self.RULE_read)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(PLC_GrammarParser.T__19)
            self.state = 157
            self.match(PLC_GrammarParser.ID)
            self.state = 162
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 158
                self.match(PLC_GrammarParser.T__1)
                self.state = 159
                self.match(PLC_GrammarParser.ID)
                self.state = 164
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
        self.enterRule(localctx, 32, self.RULE_write)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(PLC_GrammarParser.T__20)
            self.state = 166
            self.expression()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 167
                self.match(PLC_GrammarParser.T__1)
                self.state = 168
                self.expression()
                self.state = 173
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

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.StatContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.StatContext,i)


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
        self.enterRule(localctx, 34, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(PLC_GrammarParser.T__21)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 137396359170) != 0):
                self.state = 175
                self.stat()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 181
            self.match(PLC_GrammarParser.T__22)
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


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.StatContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.StatContext,i)


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
        self.enterRule(localctx, 36, self.RULE_ifCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(PLC_GrammarParser.T__23)
            self.state = 184
            self.match(PLC_GrammarParser.T__17)
            self.state = 185
            self.expression()
            self.state = 186
            self.match(PLC_GrammarParser.T__18)
            self.state = 187
            self.stat()
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 188
                self.match(PLC_GrammarParser.T__24)
                self.state = 189
                self.stat()


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


        def stat(self):
            return self.getTypedRuleContext(PLC_GrammarParser.StatContext,0)


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
        self.enterRule(localctx, 38, self.RULE_whileCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(PLC_GrammarParser.T__25)
            self.state = 193
            self.match(PLC_GrammarParser.T__17)
            self.state = 194
            self.expression()
            self.state = 195
            self.match(PLC_GrammarParser.T__18)
            self.state = 196
            self.stat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PLC_GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PLC_GrammarParser.ExpressionContext,i)


        def stat(self):
            return self.getTypedRuleContext(PLC_GrammarParser.StatContext,0)


        def getRuleIndex(self):
            return PLC_GrammarParser.RULE_forCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForCondition" ):
                listener.enterForCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForCondition" ):
                listener.exitForCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForCondition" ):
                return visitor.visitForCondition(self)
            else:
                return visitor.visitChildren(self)




    def forCondition(self):

        localctx = PLC_GrammarParser.ForConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_forCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(PLC_GrammarParser.T__26)
            self.state = 199
            self.match(PLC_GrammarParser.T__17)
            self.state = 200
            self.expression()
            self.state = 201
            self.match(PLC_GrammarParser.T__0)
            self.state = 202
            self.expression()
            self.state = 203
            self.match(PLC_GrammarParser.T__0)
            self.state = 204
            self.expression()
            self.state = 205
            self.match(PLC_GrammarParser.T__18)
            self.state = 206
            self.stat()
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
        self.enterRule(localctx, 42, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
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





