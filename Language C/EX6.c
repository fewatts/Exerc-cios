#include <stdio.h>

int main(){
    float nota_1, nota_2, nota_final;
    
    printf("Digite a primeira nota:\n");
    scanf("%f", &nota_1);

    printf("Digite a segunda nota:\n");
    scanf("%f", &nota_2);

    nota_final = (nota_1 + nota_2) / 2;
    if(nota_final >= 7){
        printf("Aprovado!, sua nota final foi %f \n", nota_final);
    } else {
        printf("Reprovado\n");
    }
}