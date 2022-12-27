soma = 0
for c in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
print(f'A soma dos valores pares é de {soma}')
