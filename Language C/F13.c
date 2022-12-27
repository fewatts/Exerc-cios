#include<stdio.h>
void main(){
    int n, count, p = 1, i = 1;
    printf("Digite um número inteiro positivo: ");
    scanf("%d", &n);

    for(count = 1; count <= n; count++){
        if(count % 2 == 0){
            p += count;
        }else{
            i += count;
        }
    }
    printf("Valor de p: %d\nValor de i: %d", p, i);
}