matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite o ({lin},{col}) valor: '))
print('¬' * 30)
print(f'{"MATRIZ":^30}')
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^7}]', end='')
    print()
