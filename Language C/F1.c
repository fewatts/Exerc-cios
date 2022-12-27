#include <string.h>
#include <stdio.h>

int main(){
    char str1[100], str2[100], str3[100];
    puts("Digite uma frase: ");
    gets(str1);
    strcpy(str2, str1);
    strcpy(str3, "Voce digitou a frase:");
    printf("%s %s\n", str3, str2);
}
