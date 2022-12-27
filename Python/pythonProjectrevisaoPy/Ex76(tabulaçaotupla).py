listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 130,
            'Canetas', 20,
            'Livros', 35.90)
print('¬' * 40)
print(f'{"PREÇOS":^40}')
print('¬' * 40)
for pos in range(0, len(listagem)):
    if pos == 0 or pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'{listagem[pos]:>7.2f}')
print('¬' * 40)
