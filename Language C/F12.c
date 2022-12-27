#include<stdio.h>

int func(int n){
    if(n == 0){
        return 0;
    }else{
        return(3 * n + func(n - 1));
    }
}

void main(){
    int a, b;
    printf("Valor inteiro:");
    scanf("%d\n", &a);
    b = func(a);
    printf("%d\n", b);
}
