#include<stdio.h>

void incr_vetor(int *v, int tam){
    int i;
    for(i = 0; i < tam; i++){
        v[i]++;
    }
}
void main(){
    int a[] = {1, 3, 5};
    incr_vetor(a, 3);
    printf("%d %d %d\n", a[0], a[1], a[2]);
}
