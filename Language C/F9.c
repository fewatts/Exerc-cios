#include<stdio.h>
#include<string.h>

typedef struct F9{
    char nome[100];
    char sexo;
    float peso;
    float altura;
} Pessoa;
#define QUANTIDADE_DE_PESSOAS 3

int main(){
    int i;
    float imc;
    char nomeloc[100];
    Pessoa pessoas[QUANTIDADE_DE_PESSOAS];
    printf("Campos: nome, altura, peso, sexo\n");
    for(i = 0; i < QUANTIDADE_DE_PESSOAS; i++){
        printf("\nInforme os dados das pessoas(%i) (Nome, altura, peso e sexo):  ", i + 1);
        scanf("%s %f %f %c", pessoas[i].nome, &pessoas[i].altura, &pessoas[i].peso, &pessoas[i].sexo);
    }
    printf("\nInforme o nome da pessoa: ");
    scanf("%s", &nomeloc);
    printf("\nSEXO\tNOME\tIMC");
    for(i = 0; (i < QUANTIDADE_DE_PESSOAS); i++){
        if(strcmp(pessoas[i].nome, nomeloc) == 0){
            float imc = pessoas[i].peso / (pessoas[i].altura * pessoas[i].altura);
            printf("\n%c\t%s\t%.2f\n", pessoas[i].sexo, pessoas[i].nome, imc);
            break;
        }
    }
    return 0;
}
