#include <stdio.h>
 int main(){
    //Declarando notas
    float notas[5] = {7, 8, 9.4, 9.5, 6};
    int i;
    printf("Exibição de notas do vetor: \n\n");
   for(i = 0; i <=4 ; i++){
      printf("nota[%d] = %.1f\n", i, notas[i]);
   }
   return 0;
 }
