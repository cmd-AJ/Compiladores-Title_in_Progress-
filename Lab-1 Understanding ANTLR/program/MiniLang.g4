grammar MiniLang;

prog: stat+ ;

stat
    : expr NEWLINE                      # printExpr
    | ID '=' expr NEWLINE              # assign
    | 'if' expr ':' block              # ifStmt
    | 'while' expr ':' block           # whileStmt
    | NEWLINE                          # blank
    ;

block: '{' stat+ '}' ; // simple block for now (e.g., { x = 3 })

expr
    : expr ('*'|'/') expr              # MulDiv
    | expr ('+'|'-') expr              # AddSub
    | expr ('=='|'!='|'<'|'>'|'<='|'>=') expr  # comparison
    | INT                              # int
    | ID                               # id
    | '(' expr ')'                     # parens
    ;

MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;
EQ  : '==' ;
NEQ : '!=' ;
LT  : '<' ;
GT  : '>' ;
LE  : '<=' ;
GE  : '>=' ;

IF  : 'if' ;
WHILE : 'while' ;
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
INT : [0-9]+ ;
NEWLINE : '\r'? '\n' ;
WS  : [ \t]+ -> skip ;
