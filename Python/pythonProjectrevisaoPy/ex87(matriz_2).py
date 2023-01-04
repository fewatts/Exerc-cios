matrix = [[0, 0, 0], 
          [0, 0, 0], 
          [0, 0, 0]]
sump =  soma_3col = 0
for lin in range(0, 3):
    for col in range(0, 3):
        matrix[lin][col] = int(input(f'Digite o [{lin}], [{col}] valor: '))
print('¬' * 30)
print(f'{"MATRIZ":^30}')
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matrix[lin][col]:^6}]', end='')
        if matrix[lin][col] % 2 == 0:
            sump += matrix[lin][col]
    print()
print('¬' * 30)
print(f'A soma dos valores pares da matriz é {sump}')
for lin in range(0, 3):
    soma_3col += matrix[lin][2]
print(f'A soma da última coluna é {soma_3col}')
for col in range(0, 3):
    if col == 0:
        maior = matrix[1][col]
    elif matrix[1][col] > maior:
        maior = matrix[1][col]
print(f'O maior valor é {maior}')
