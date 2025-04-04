grammar Calc;

prog: stat+ ;

stat: 'let' ID '=' expr ';'          # assign
    | expr ';'                       # exprStatement
    ;

expr: expr op=('*'|'/') expr         # MulDiv
    | expr op=('+'|'-') expr         # AddSub
    | INT                            # int
    | ID                             # var
    | '(' expr ')'                   # parens
    ;

ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;