#include<stdio.h>

int main(){
    int i;
    float notas[5];

    printf("Preenchendo o vetor\n\n");
    for(i = 0; i <= 4; i++){
        printf("Digite a %d nota:", i + 1);
        scanf("%f", &notas[i]);
        printf("\n¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n");
    }
    printf("Exibindo os valores do vetor \n\n");
    for(i = 0; i <=4; i++){
        printf("Nota %d = %.1f\n", i + 1, notas[i]);
    }
    return 0;
}
