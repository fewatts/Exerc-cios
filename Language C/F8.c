#include<stdio.h>
int main(){

    int i;
    float classe[lin][col] = {{8.5, 7.0, 8.5, 10.0},
                              {3.0, 4.0, 6.0, 5.5},
                              {7.0, 7.5, 6.0, 5.0}};
    for(lin = 0; lin <= 3; lin++){
        printf("%.2f", classe[lin]);
        for(col = 0; col <= 4; col++){
            printf("%.2f", classe[col]);
        }
    }
}