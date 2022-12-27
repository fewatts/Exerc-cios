#include <stdio.h>

int main(){
    int dado;

    printf("Digite o valor do dado:\n");
    scanf("%d", &dado);
    
    dado++;
    printf("O dado após incremento de 1 unidade: %d\n");

    dado--;
    printf("O dado após decremento de 1 unidade: %d\n", dado);

    dado *= dado;
    printf("O dado ao quadrado: %d\n", dado);

    dado /= 20;
    printf("O dado dividido por 20: %d\n", dado);

    dado += 5;
    printf("O dado incrementado com 5 unidades: %d\n", dado);
}