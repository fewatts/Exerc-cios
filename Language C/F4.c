#include<stdio.h>
#include<string.h>

int main(){

    int x, tam, ca, ce, ci, co, cu;
    char nome[30];
    ca = ce = ci = co = cu = 0;

    printf("Digite uma frase: ");
    gets(nome);
    tam = strlen(nome);

    for(x = 1; x <= tam - 1; x++){
        if(nome[x] == 'a' || nome[x] == 'A'){
            ca++;
        }else{
            if(nome[x] == 'e' || nome[x] == 'E'){
                ce++;
            }else{
                if(nome[x] == 'i' || nome[x] == 'I'){
                    ci++;
                }else{
                    if(nome[x] == 'o' || nome[x] == 'O'){
                        co++;
                    }else{
                        if(nome[x] == 'u' || nome[x] == 'U'){
                            cu++;
                        }
                    }
                }
            }
        }
    }
    printf("%d - a, ", ca);
    printf("%d - e, ", ce);
    printf("%d - i, ", ci);
    printf("%d - o, ", co);
    printf("%d - u, ", cu);
    printf("\n\n");
    printf("PAUSE");
    return 0;
}