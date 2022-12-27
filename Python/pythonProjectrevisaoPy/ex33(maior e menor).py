a = int(input('Digite um número inteiro: '))
b = int(input('Digite um número inteiro: '))
c = int(input('Digite um número inteiro: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor foi {menor}')
print(f'O maior valor foi {maior}')
