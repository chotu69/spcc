%{
#include <stdio.h>
%}

%%
[0-9]+          { printf("Number: %s\n", yytext); }
if|else|while|int   { printf("Keyword: %s\n", yytext); }
[a-zA-Z]+       { printf("Word: %s\n", yytext); }
[ \t\n]         ;  /* Ignore whitespace and newline characters */
.               ;  /* Ignore any other characters */

%%

int yywrap(void) {
    return 1; /* Indicate that we have reached the end of input */
}

int main(void) {
    yylex();
    return 0;
}