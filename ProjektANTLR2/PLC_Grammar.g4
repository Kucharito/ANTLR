grammar PLC_Grammar;

prog: statement+; // The start rule; begin parsing here.

statement
    :';'
    | declaration ';'
    | expression ';'
    | read ';'
    | write ';'
    | block 
    | ifCondition 
    | whileCondition
    | forCondition
    ;

declaration: type ID (',' ID)*; // Variable declaration with optional initialization

//read and write
read: 'read' ID (','ID)*; // Read statement for multiple variables
write: 'write' expression (','expression)*; // Write statement for multiple expressions

//block
block: '{' statement* '}'; // Block of statements enclosed in braces

//ifCondition
ifCondition: 'if' '(' expression ')' statement ('else' statement)?; // If-else condition

whileCondition: 'while' '(' expression ')' statement; // While loop condition

forCondition: 'for' '(' expression ';' expression ';' expression ')' statement; // For loop condition

expression
    : assignment
    ;

assignment
    : or ('=' assignment)? 
    ;

or
    : and ( '||' and )* 
    ;

and
    : equality ( '&&' equality )* 
    ;

equality
    : relational ( ('==' | '!=') relational )* 
    ;

relational
    : additive ( ('<' | '>' ) additive )* 
    ;

additive
    : multiplicative ( ('+' | '-'| '.') multiplicative )* 
    ;

multiplicative
    : unary ( ('*' | '/'| '%') unary )* 
    ;

unary
    : ('-' | '!')? primary 
    ;

primary
    : '(' expression ')'
    | literal
    | ID
    ;

literal
    : INT
    | FLOAT
    | BOOL
    | STRING
    ;

type
        : 'int'
        | 'float'
        | 'bool'
        | 'string'
        ;

ID : [a-zA-Z] [a-zA-Z0-9]* ; // match identifiers
INT : [0-9]+ ; // match integers
FLOAT : [0-9]+ '.' [0-9]+ ; // match floating point numbers
BOOL: 'true' | 'false' ; // match boolean values
STRING : '"' ( ~["\\] | '\\' . )* '"' ; // match strings
NEWLINE : '\r'? '\n' ; // return newlines to parser (is end-statement signal)
WS : [ \t]+ -> skip ; // toss out whitespace
COMMENT : '//' ~[\r\n]* -> skip ; // single line comments