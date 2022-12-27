#include <stdio.h>
void main()
{
int a=45;
int b=5;
int c, d;
c = a/b;
d = a % b--;
printf("%d %d %d %d\n", a, b, c, d); 
}