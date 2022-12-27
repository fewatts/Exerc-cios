lista = []
maior =  menor = i = 0
for i in range(0, 5):
    lista.append(int(input(f'Digite o valor {i}: ')))
    if i == 0:
        maior = lista[i]
        menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print('¬' * 45)
print(f'A lista formada foi a seguinte: {lista}')
print(f'O maior valor é {maior} e ele está localizado nas posições ', end='')
for p, v in enumerate(lista):
    if v == maior:
        print(f'{p}...', end='')
print(f'\nO menor valor é {menor} e ele está localizado nas posições ', end='')
for p, v in enumerate(lista):
    if v == menor:
        print(f'{p}...', end='')
