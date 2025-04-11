// Generated from c:/Users/adamk/OneDrive/Počítač/antlr/ProjektANTLR/PLC_Grammar.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class PLC_GrammarParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, ID=30, INT=31, FLOAT=32, 
		BOOL=33, STRING=34, NEWLINE=35, WS=36, COMMENT=37;
	public static final int
		RULE_prog = 0, RULE_statement = 1, RULE_declaration = 2, RULE_read = 3, 
		RULE_write = 4, RULE_block = 5, RULE_ifCondition = 6, RULE_whileCondition = 7, 
		RULE_expression = 8, RULE_assignment = 9, RULE_or = 10, RULE_and = 11, 
		RULE_equality = 12, RULE_relational = 13, RULE_additive = 14, RULE_multiplicative = 15, 
		RULE_unary = 16, RULE_primary = 17, RULE_literal = 18, RULE_type = 19;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "statement", "declaration", "read", "write", "block", "ifCondition", 
			"whileCondition", "expression", "assignment", "or", "and", "equality", 
			"relational", "additive", "multiplicative", "unary", "primary", "literal", 
			"type"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "','", "'read'", "'write'", "'{'", "'}'", "'if'", "'('", 
			"')'", "'else'", "'while'", "'='", "'||'", "'&&'", "'=='", "'!='", "'<'", 
			"'>'", "'+'", "'-'", "'.'", "'*'", "'/'", "'%'", "'!'", "'int'", "'float'", 
			"'bool'", "'string'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "ID", "INT", "FLOAT", "BOOL", "STRING", 
			"NEWLINE", "WS", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "PLC_Grammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PLC_GrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(40);
				statement();
				}
				}
				setState(43); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 34327235002L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ReadContext read() {
			return getRuleContext(ReadContext.class,0);
		}
		public WriteContext write() {
			return getRuleContext(WriteContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public IfConditionContext ifCondition() {
			return getRuleContext(IfConditionContext.class,0);
		}
		public WhileConditionContext whileCondition() {
			return getRuleContext(WhileConditionContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(61);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(45);
				match(T__0);
				}
				break;
			case T__25:
			case T__26:
			case T__27:
			case T__28:
				enterOuterAlt(_localctx, 2);
				{
				setState(46);
				declaration();
				setState(47);
				match(T__0);
				}
				break;
			case T__7:
			case T__19:
			case T__24:
			case ID:
			case INT:
			case FLOAT:
			case BOOL:
			case STRING:
				enterOuterAlt(_localctx, 3);
				{
				setState(49);
				expression();
				setState(50);
				match(T__0);
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 4);
				{
				setState(52);
				read();
				setState(53);
				match(T__0);
				}
				break;
			case T__3:
				enterOuterAlt(_localctx, 5);
				{
				setState(55);
				write();
				setState(56);
				match(T__0);
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 6);
				{
				setState(58);
				block();
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 7);
				{
				setState(59);
				ifCondition();
				}
				break;
			case T__10:
				enterOuterAlt(_localctx, 8);
				{
				setState(60);
				whileCondition();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends ParserRuleContext {
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public List<TerminalNode> ID() { return getTokens(PLC_GrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(PLC_GrammarParser.ID, i);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			type();
			setState(64);
			match(ID);
			setState(69);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(65);
				match(T__1);
				setState(66);
				match(ID);
				}
				}
				setState(71);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReadContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(PLC_GrammarParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(PLC_GrammarParser.ID, i);
		}
		public ReadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_read; }
	}

	public final ReadContext read() throws RecognitionException {
		ReadContext _localctx = new ReadContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_read);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			match(T__2);
			setState(73);
			match(ID);
			setState(78);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(74);
				match(T__1);
				setState(75);
				match(ID);
				}
				}
				setState(80);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WriteContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public WriteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_write; }
	}

	public final WriteContext write() throws RecognitionException {
		WriteContext _localctx = new WriteContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_write);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(T__3);
			setState(82);
			expression();
			setState(87);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(83);
				match(T__1);
				setState(84);
				expression();
				}
				}
				setState(89);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlockContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(T__4);
			setState(94);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 34327235002L) != 0)) {
				{
				{
				setState(91);
				statement();
				}
				}
				setState(96);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(97);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfConditionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public IfConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifCondition; }
	}

	public final IfConditionContext ifCondition() throws RecognitionException {
		IfConditionContext _localctx = new IfConditionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_ifCondition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			match(T__6);
			setState(100);
			match(T__7);
			setState(101);
			expression();
			setState(102);
			match(T__8);
			setState(103);
			statement();
			setState(106);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(104);
				match(T__9);
				setState(105);
				statement();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileConditionContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public WhileConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileCondition; }
	}

	public final WhileConditionContext whileCondition() throws RecognitionException {
		WhileConditionContext _localctx = new WhileConditionContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_whileCondition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(108);
			match(T__10);
			setState(109);
			match(T__7);
			setState(110);
			expression();
			setState(111);
			match(T__8);
			setState(112);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			assignment();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public OrContext or() {
			return getRuleContext(OrContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_assignment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			or();
			setState(119);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__11) {
				{
				setState(117);
				match(T__11);
				setState(118);
				assignment();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OrContext extends ParserRuleContext {
		public List<AndContext> and() {
			return getRuleContexts(AndContext.class);
		}
		public AndContext and(int i) {
			return getRuleContext(AndContext.class,i);
		}
		public OrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_or; }
	}

	public final OrContext or() throws RecognitionException {
		OrContext _localctx = new OrContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_or);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			and();
			setState(126);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__12) {
				{
				{
				setState(122);
				match(T__12);
				setState(123);
				and();
				}
				}
				setState(128);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AndContext extends ParserRuleContext {
		public List<EqualityContext> equality() {
			return getRuleContexts(EqualityContext.class);
		}
		public EqualityContext equality(int i) {
			return getRuleContext(EqualityContext.class,i);
		}
		public AndContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_and; }
	}

	public final AndContext and() throws RecognitionException {
		AndContext _localctx = new AndContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_and);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			equality();
			setState(134);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__13) {
				{
				{
				setState(130);
				match(T__13);
				setState(131);
				equality();
				}
				}
				setState(136);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EqualityContext extends ParserRuleContext {
		public List<RelationalContext> relational() {
			return getRuleContexts(RelationalContext.class);
		}
		public RelationalContext relational(int i) {
			return getRuleContext(RelationalContext.class,i);
		}
		public EqualityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equality; }
	}

	public final EqualityContext equality() throws RecognitionException {
		EqualityContext _localctx = new EqualityContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_equality);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			relational();
			setState(142);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__14 || _la==T__15) {
				{
				{
				setState(138);
				_la = _input.LA(1);
				if ( !(_la==T__14 || _la==T__15) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(139);
				relational();
				}
				}
				setState(144);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RelationalContext extends ParserRuleContext {
		public List<AdditiveContext> additive() {
			return getRuleContexts(AdditiveContext.class);
		}
		public AdditiveContext additive(int i) {
			return getRuleContext(AdditiveContext.class,i);
		}
		public RelationalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relational; }
	}

	public final RelationalContext relational() throws RecognitionException {
		RelationalContext _localctx = new RelationalContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_relational);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			additive();
			setState(150);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__16 || _la==T__17) {
				{
				{
				setState(146);
				_la = _input.LA(1);
				if ( !(_la==T__16 || _la==T__17) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(147);
				additive();
				}
				}
				setState(152);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AdditiveContext extends ParserRuleContext {
		public List<MultiplicativeContext> multiplicative() {
			return getRuleContexts(MultiplicativeContext.class);
		}
		public MultiplicativeContext multiplicative(int i) {
			return getRuleContext(MultiplicativeContext.class,i);
		}
		public AdditiveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_additive; }
	}

	public final AdditiveContext additive() throws RecognitionException {
		AdditiveContext _localctx = new AdditiveContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_additive);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(153);
			multiplicative();
			setState(158);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3670016L) != 0)) {
				{
				{
				setState(154);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3670016L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(155);
				multiplicative();
				}
				}
				setState(160);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MultiplicativeContext extends ParserRuleContext {
		public List<UnaryContext> unary() {
			return getRuleContexts(UnaryContext.class);
		}
		public UnaryContext unary(int i) {
			return getRuleContext(UnaryContext.class,i);
		}
		public MultiplicativeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicative; }
	}

	public final MultiplicativeContext multiplicative() throws RecognitionException {
		MultiplicativeContext _localctx = new MultiplicativeContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_multiplicative);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			unary();
			setState(166);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 29360128L) != 0)) {
				{
				{
				setState(162);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 29360128L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(163);
				unary();
				}
				}
				setState(168);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnaryContext extends ParserRuleContext {
		public PrimaryContext primary() {
			return getRuleContext(PrimaryContext.class,0);
		}
		public UnaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unary; }
	}

	public final UnaryContext unary() throws RecognitionException {
		UnaryContext _localctx = new UnaryContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_unary);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(170);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__19 || _la==T__24) {
				{
				setState(169);
				_la = _input.LA(1);
				if ( !(_la==T__19 || _la==T__24) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(172);
			primary();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public TerminalNode ID() { return getToken(PLC_GrammarParser.ID, 0); }
		public PrimaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primary; }
	}

	public final PrimaryContext primary() throws RecognitionException {
		PrimaryContext _localctx = new PrimaryContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_primary);
		try {
			setState(180);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__7:
				enterOuterAlt(_localctx, 1);
				{
				setState(174);
				match(T__7);
				setState(175);
				expression();
				setState(176);
				match(T__8);
				}
				break;
			case INT:
			case FLOAT:
			case BOOL:
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(178);
				literal();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 3);
				{
				setState(179);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(PLC_GrammarParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(PLC_GrammarParser.FLOAT, 0); }
		public TerminalNode BOOL() { return getToken(PLC_GrammarParser.BOOL, 0); }
		public TerminalNode STRING() { return getToken(PLC_GrammarParser.STRING, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(182);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 32212254720L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(184);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1006632960L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001%\u00bb\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0001\u0000\u0004\u0000*\b\u0000\u000b\u0000"+
		"\f\u0000+\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		">\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002"+
		"D\b\u0002\n\u0002\f\u0002G\t\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0005\u0003M\b\u0003\n\u0003\f\u0003P\t\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0005\u0004V\b\u0004\n\u0004\f\u0004"+
		"Y\t\u0004\u0001\u0005\u0001\u0005\u0005\u0005]\b\u0005\n\u0005\f\u0005"+
		"`\t\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006k\b\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0003\tx\b\t\u0001\n\u0001\n"+
		"\u0001\n\u0005\n}\b\n\n\n\f\n\u0080\t\n\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0005\u000b\u0085\b\u000b\n\u000b\f\u000b\u0088\t\u000b\u0001\f"+
		"\u0001\f\u0001\f\u0005\f\u008d\b\f\n\f\f\f\u0090\t\f\u0001\r\u0001\r\u0001"+
		"\r\u0005\r\u0095\b\r\n\r\f\r\u0098\t\r\u0001\u000e\u0001\u000e\u0001\u000e"+
		"\u0005\u000e\u009d\b\u000e\n\u000e\f\u000e\u00a0\t\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0005\u000f\u00a5\b\u000f\n\u000f\f\u000f\u00a8\t\u000f"+
		"\u0001\u0010\u0003\u0010\u00ab\b\u0010\u0001\u0010\u0001\u0010\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0003\u0011"+
		"\u00b5\b\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0000\u0000\u0014\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \"$&\u0000\u0007\u0001\u0000\u000f\u0010"+
		"\u0001\u0000\u0011\u0012\u0001\u0000\u0013\u0015\u0001\u0000\u0016\u0018"+
		"\u0002\u0000\u0014\u0014\u0019\u0019\u0001\u0000\u001f\"\u0001\u0000\u001a"+
		"\u001d\u00bd\u0000)\u0001\u0000\u0000\u0000\u0002=\u0001\u0000\u0000\u0000"+
		"\u0004?\u0001\u0000\u0000\u0000\u0006H\u0001\u0000\u0000\u0000\bQ\u0001"+
		"\u0000\u0000\u0000\nZ\u0001\u0000\u0000\u0000\fc\u0001\u0000\u0000\u0000"+
		"\u000el\u0001\u0000\u0000\u0000\u0010r\u0001\u0000\u0000\u0000\u0012t"+
		"\u0001\u0000\u0000\u0000\u0014y\u0001\u0000\u0000\u0000\u0016\u0081\u0001"+
		"\u0000\u0000\u0000\u0018\u0089\u0001\u0000\u0000\u0000\u001a\u0091\u0001"+
		"\u0000\u0000\u0000\u001c\u0099\u0001\u0000\u0000\u0000\u001e\u00a1\u0001"+
		"\u0000\u0000\u0000 \u00aa\u0001\u0000\u0000\u0000\"\u00b4\u0001\u0000"+
		"\u0000\u0000$\u00b6\u0001\u0000\u0000\u0000&\u00b8\u0001\u0000\u0000\u0000"+
		"(*\u0003\u0002\u0001\u0000)(\u0001\u0000\u0000\u0000*+\u0001\u0000\u0000"+
		"\u0000+)\u0001\u0000\u0000\u0000+,\u0001\u0000\u0000\u0000,\u0001\u0001"+
		"\u0000\u0000\u0000->\u0005\u0001\u0000\u0000./\u0003\u0004\u0002\u0000"+
		"/0\u0005\u0001\u0000\u00000>\u0001\u0000\u0000\u000012\u0003\u0010\b\u0000"+
		"23\u0005\u0001\u0000\u00003>\u0001\u0000\u0000\u000045\u0003\u0006\u0003"+
		"\u000056\u0005\u0001\u0000\u00006>\u0001\u0000\u0000\u000078\u0003\b\u0004"+
		"\u000089\u0005\u0001\u0000\u00009>\u0001\u0000\u0000\u0000:>\u0003\n\u0005"+
		"\u0000;>\u0003\f\u0006\u0000<>\u0003\u000e\u0007\u0000=-\u0001\u0000\u0000"+
		"\u0000=.\u0001\u0000\u0000\u0000=1\u0001\u0000\u0000\u0000=4\u0001\u0000"+
		"\u0000\u0000=7\u0001\u0000\u0000\u0000=:\u0001\u0000\u0000\u0000=;\u0001"+
		"\u0000\u0000\u0000=<\u0001\u0000\u0000\u0000>\u0003\u0001\u0000\u0000"+
		"\u0000?@\u0003&\u0013\u0000@E\u0005\u001e\u0000\u0000AB\u0005\u0002\u0000"+
		"\u0000BD\u0005\u001e\u0000\u0000CA\u0001\u0000\u0000\u0000DG\u0001\u0000"+
		"\u0000\u0000EC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000F\u0005"+
		"\u0001\u0000\u0000\u0000GE\u0001\u0000\u0000\u0000HI\u0005\u0003\u0000"+
		"\u0000IN\u0005\u001e\u0000\u0000JK\u0005\u0002\u0000\u0000KM\u0005\u001e"+
		"\u0000\u0000LJ\u0001\u0000\u0000\u0000MP\u0001\u0000\u0000\u0000NL\u0001"+
		"\u0000\u0000\u0000NO\u0001\u0000\u0000\u0000O\u0007\u0001\u0000\u0000"+
		"\u0000PN\u0001\u0000\u0000\u0000QR\u0005\u0004\u0000\u0000RW\u0003\u0010"+
		"\b\u0000ST\u0005\u0002\u0000\u0000TV\u0003\u0010\b\u0000US\u0001\u0000"+
		"\u0000\u0000VY\u0001\u0000\u0000\u0000WU\u0001\u0000\u0000\u0000WX\u0001"+
		"\u0000\u0000\u0000X\t\u0001\u0000\u0000\u0000YW\u0001\u0000\u0000\u0000"+
		"Z^\u0005\u0005\u0000\u0000[]\u0003\u0002\u0001\u0000\\[\u0001\u0000\u0000"+
		"\u0000]`\u0001\u0000\u0000\u0000^\\\u0001\u0000\u0000\u0000^_\u0001\u0000"+
		"\u0000\u0000_a\u0001\u0000\u0000\u0000`^\u0001\u0000\u0000\u0000ab\u0005"+
		"\u0006\u0000\u0000b\u000b\u0001\u0000\u0000\u0000cd\u0005\u0007\u0000"+
		"\u0000de\u0005\b\u0000\u0000ef\u0003\u0010\b\u0000fg\u0005\t\u0000\u0000"+
		"gj\u0003\u0002\u0001\u0000hi\u0005\n\u0000\u0000ik\u0003\u0002\u0001\u0000"+
		"jh\u0001\u0000\u0000\u0000jk\u0001\u0000\u0000\u0000k\r\u0001\u0000\u0000"+
		"\u0000lm\u0005\u000b\u0000\u0000mn\u0005\b\u0000\u0000no\u0003\u0010\b"+
		"\u0000op\u0005\t\u0000\u0000pq\u0003\u0002\u0001\u0000q\u000f\u0001\u0000"+
		"\u0000\u0000rs\u0003\u0012\t\u0000s\u0011\u0001\u0000\u0000\u0000tw\u0003"+
		"\u0014\n\u0000uv\u0005\f\u0000\u0000vx\u0003\u0012\t\u0000wu\u0001\u0000"+
		"\u0000\u0000wx\u0001\u0000\u0000\u0000x\u0013\u0001\u0000\u0000\u0000"+
		"y~\u0003\u0016\u000b\u0000z{\u0005\r\u0000\u0000{}\u0003\u0016\u000b\u0000"+
		"|z\u0001\u0000\u0000\u0000}\u0080\u0001\u0000\u0000\u0000~|\u0001\u0000"+
		"\u0000\u0000~\u007f\u0001\u0000\u0000\u0000\u007f\u0015\u0001\u0000\u0000"+
		"\u0000\u0080~\u0001\u0000\u0000\u0000\u0081\u0086\u0003\u0018\f\u0000"+
		"\u0082\u0083\u0005\u000e\u0000\u0000\u0083\u0085\u0003\u0018\f\u0000\u0084"+
		"\u0082\u0001\u0000\u0000\u0000\u0085\u0088\u0001\u0000\u0000\u0000\u0086"+
		"\u0084\u0001\u0000\u0000\u0000\u0086\u0087\u0001\u0000\u0000\u0000\u0087"+
		"\u0017\u0001\u0000\u0000\u0000\u0088\u0086\u0001\u0000\u0000\u0000\u0089"+
		"\u008e\u0003\u001a\r\u0000\u008a\u008b\u0007\u0000\u0000\u0000\u008b\u008d"+
		"\u0003\u001a\r\u0000\u008c\u008a\u0001\u0000\u0000\u0000\u008d\u0090\u0001"+
		"\u0000\u0000\u0000\u008e\u008c\u0001\u0000\u0000\u0000\u008e\u008f\u0001"+
		"\u0000\u0000\u0000\u008f\u0019\u0001\u0000\u0000\u0000\u0090\u008e\u0001"+
		"\u0000\u0000\u0000\u0091\u0096\u0003\u001c\u000e\u0000\u0092\u0093\u0007"+
		"\u0001\u0000\u0000\u0093\u0095\u0003\u001c\u000e\u0000\u0094\u0092\u0001"+
		"\u0000\u0000\u0000\u0095\u0098\u0001\u0000\u0000\u0000\u0096\u0094\u0001"+
		"\u0000\u0000\u0000\u0096\u0097\u0001\u0000\u0000\u0000\u0097\u001b\u0001"+
		"\u0000\u0000\u0000\u0098\u0096\u0001\u0000\u0000\u0000\u0099\u009e\u0003"+
		"\u001e\u000f\u0000\u009a\u009b\u0007\u0002\u0000\u0000\u009b\u009d\u0003"+
		"\u001e\u000f\u0000\u009c\u009a\u0001\u0000\u0000\u0000\u009d\u00a0\u0001"+
		"\u0000\u0000\u0000\u009e\u009c\u0001\u0000\u0000\u0000\u009e\u009f\u0001"+
		"\u0000\u0000\u0000\u009f\u001d\u0001\u0000\u0000\u0000\u00a0\u009e\u0001"+
		"\u0000\u0000\u0000\u00a1\u00a6\u0003 \u0010\u0000\u00a2\u00a3\u0007\u0003"+
		"\u0000\u0000\u00a3\u00a5\u0003 \u0010\u0000\u00a4\u00a2\u0001\u0000\u0000"+
		"\u0000\u00a5\u00a8\u0001\u0000\u0000\u0000\u00a6\u00a4\u0001\u0000\u0000"+
		"\u0000\u00a6\u00a7\u0001\u0000\u0000\u0000\u00a7\u001f\u0001\u0000\u0000"+
		"\u0000\u00a8\u00a6\u0001\u0000\u0000\u0000\u00a9\u00ab\u0007\u0004\u0000"+
		"\u0000\u00aa\u00a9\u0001\u0000\u0000\u0000\u00aa\u00ab\u0001\u0000\u0000"+
		"\u0000\u00ab\u00ac\u0001\u0000\u0000\u0000\u00ac\u00ad\u0003\"\u0011\u0000"+
		"\u00ad!\u0001\u0000\u0000\u0000\u00ae\u00af\u0005\b\u0000\u0000\u00af"+
		"\u00b0\u0003\u0010\b\u0000\u00b0\u00b1\u0005\t\u0000\u0000\u00b1\u00b5"+
		"\u0001\u0000\u0000\u0000\u00b2\u00b5\u0003$\u0012\u0000\u00b3\u00b5\u0005"+
		"\u001e\u0000\u0000\u00b4\u00ae\u0001\u0000\u0000\u0000\u00b4\u00b2\u0001"+
		"\u0000\u0000\u0000\u00b4\u00b3\u0001\u0000\u0000\u0000\u00b5#\u0001\u0000"+
		"\u0000\u0000\u00b6\u00b7\u0007\u0005\u0000\u0000\u00b7%\u0001\u0000\u0000"+
		"\u0000\u00b8\u00b9\u0007\u0006\u0000\u0000\u00b9\'\u0001\u0000\u0000\u0000"+
		"\u0010+=ENW^jw~\u0086\u008e\u0096\u009e\u00a6\u00aa\u00b4";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}