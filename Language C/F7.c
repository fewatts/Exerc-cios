#include<stdio.h>

int main(){

    float t[3];
    int i;
    float soma, media, resultado;

    soma = 0;
    for(i = 0; i <= 2; i++){
        printf("Digite uma temperatura %d: ", i);
        scanf("%f", &t[i]);
        soma += t[i];
    }//tudo ok aqui
    media = soma / 3;
    for(i = 0; i <= 2; i++){
        resultado = media - t[i];
        printf("\nA diferença entre as temperaturas e a media:\n%.2f - %.2f = %.2f", media, t[i], resultado);
    }//ok
}