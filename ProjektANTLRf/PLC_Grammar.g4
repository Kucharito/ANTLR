grammar PLC_Grammar;

prog: stat*;

stat
    : ';'               // empty statement
    | declaration ';'   // declaration statement
    | expression ';'    // expression statement
    | read ';'          // read statement
    | write ';'         // write statement
    | block             // block statement
    | ifCondition       // if statement
    | whileCondition    // while statement
    | forCondition      // for statement
    ;

declaration : type ID (',' ID)*; // variable declaration

expression
    : assignement
    ;

assignement
    : concatExpression ('=' assignement)?     // assignment operator
    ;

concatExpression
    : orExpression ('<<' orExpression)*
    ;

orExpression
    : andExpression ( '||' andExpression )*        // logical OR operator
    ;

andExpression
    : equality ( '&&' equality )* // logical AND operator
    ;

equality
    : relational ( ('==' | '!=') relational )* // equality operator
    ;

relational
    : additive ( ('<' | '>') additive )* // relational operators
    ;

additive
    : multiplicative ( ('+' | '-' | '.') multiplicative )* // additive operators
    ;

multiplicative
    : unary ( ('*' | '/' | '%') unary )* // multiplicative operators
    ;

unary
    : ('-' | '!')? primary // unary operators
    ;

primary
    : '(' expression ')' // parenthesis
    | ID // variable reference
    | literal // literal values
    ;

literal
    : INT // integer literal
    | FLOAT // float literal
    | BOOL // boolean literal
    | STRING // string literal
    ;



read : 'read' ID (',' ID)* ;                            // read statement
write : 'write' expression (',' expression)* ;          // write statement
block: '{' stat* '}' ;
ifCondition: 'if' '(' expression ')' stat ('else' stat)? ; // if statement with optional else
whileCondition: 'while' '(' expression ')' stat ; // while statement
forCondition: 'for' '(' expression ';' expression ';' expression ')' stat ; // for statement

BOOL : 'true' | 'false' ;                       // match booleans
STRING : '"' ( ~["\\] | '\\' . )* '"' ;
ID : [a-zA-Z][a-zA-Z0-9]*  ;                                // match identifiers
INT : [0-9]+ ;                                  // match integers
FLOAT : [0-9]+ '.' [0-9]+ ;                     // match floats       // match strings with optional escape sequences

type : 'int' | 'float' | 'bool' | 'string' ;    // variable types

WS : [ \t\r\n]+ -> skip ; // toto zahŕňa aj nové riadky
COMMENT : '//' ~[\r\n]* -> skip ;               // skip single-line comments
