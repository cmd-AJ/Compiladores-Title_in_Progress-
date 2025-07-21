grammar SimpleLang;

prog: stat+ ;

stat: expr NEWLINE ;

expr: expr op=('*'|'/') expr       # MulDiv
    | expr op=('+'|'-') expr       # AddSub
    | expr op='%' expr             # Mod
    | expr op='^' expr             # Pow
    | expr op=('<' | '>' | '<=' | '>=' | '==' | '!=') expr  # Relational
    | INT                          # Int
    | FLOAT                        # Float
    | STRING                       # String
    | CHAR                         # Char
    | BOOL                         # Bool
    | '(' expr ')'                 # Parens
    ;

INT: [0-9]+ ;
FLOAT: [0-9]+'.'[0-9]* ;
STRING: '"' .*? '"' ;
CHAR: '\'' . '\'' ; // carácter único entre comillas simples
BOOL: 'true' | 'false' ;
NEWLINE: '\r'? '\n' ;
WS: [ \t]+ -> skip ;
