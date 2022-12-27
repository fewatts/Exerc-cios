contagem = 0
soma = 0
for count in range(1, 501, 2):
    if count % 3 == 0:
        contagem += 1
        soma += count
print(f'A soma dos {contagem} números é igual a {soma}')
