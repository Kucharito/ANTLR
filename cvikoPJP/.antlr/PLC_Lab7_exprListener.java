// Generated from c:/Users/adamk/OneDrive/Počítač/antlr/cvikoPJP/PLC_Lab7_expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PLC_Lab7_exprParser}.
 */
public interface PLC_Lab7_exprListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PLC_Lab7_exprParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(PLC_Lab7_exprParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link PLC_Lab7_exprParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(PLC_Lab7_exprParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link PLC_Lab7_exprParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterStat(PLC_Lab7_exprParser.StatContext ctx);
	/**
	 * Exit a parse tree produced by {@link PLC_Lab7_exprParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitStat(PLC_Lab7_exprParser.StatContext ctx);
	/**
	 * Enter a parse tree produced by {@link PLC_Lab7_exprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(PLC_Lab7_exprParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link PLC_Lab7_exprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(PLC_Lab7_exprParser.ExprContext ctx);
}