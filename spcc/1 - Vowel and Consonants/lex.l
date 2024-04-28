%{
#include<stdio.h>
int v=0,c=0;
%}

%%
[\t\n]+;
[aeiouAEIOU] {v++;}
[^aeiouAEIOU] {c++;}
%%

int main(){
	printf("\nEnter the string: ");
	yylex();
	printf("No. of vowels are %d: \n",v);
	printf("No. of consonants are %d: \n",c);
}

int yywrap(){
	return 1;
}