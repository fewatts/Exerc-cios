
lista_c = [[], []]
for n in range(0, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        lista_c[0].append(num)
    else:
        lista_c[1].append(num)
print('¬' * 120)
print(f'Números pares: {sorted(lista_c[0])}')
print(f'Números ímpares: {sorted(lista_c[1])}')
