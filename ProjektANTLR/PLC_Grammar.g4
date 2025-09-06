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
    | fileWrite ';'
    ;

//declaration: type ID (',' ID)* ('='STRING); 
declaration: type ID (',' ID)* ('=' expression)?; 

//read and write
read: 'read' ID (','ID)*; 
write: 'write' expression (','expression)*; 

//block
block: '{' statement* '}'; 

//ifCondition
ifCondition: 'if' '(' expression ')' statement ('else' statement)?; // If-else condition

whileCondition: 'while' '(' expression ')' statement; // While loop condition

fileWrite: ID ('<<' assignment)+;

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
        | 'FILE'
        ;
        
FILE : 'file'; // match file identifiers
ID : [a-zA-Z] [a-zA-Z0-9]* ; // match identifiers
INT : [0-9]+ ; // match integers
FLOAT : [0-9]+ '.' [0-9]+ ; // match floating point numbers
BOOL: 'true' | 'false' ; // match boolean values
STRING : '"' ( ~["\\] | '\\' . )* '"' ; // match strings
NEWLINE : '\r'? '\n' -> skip;
WS : [ \t]+ -> skip ; // toss out whitespace
COMMENT : '//' ~[\r\n]* -> skip ; // single line comments
