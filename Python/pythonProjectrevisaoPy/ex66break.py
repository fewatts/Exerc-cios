count = soma = 0
while True:
    n = int(input('Digite um número inteiro: [999 para parar] '))
    if n == 999:
        break
    count += 1
    soma += n
print(f'A soma entre os números é de {soma} e no total foram {count} valores digitados')
