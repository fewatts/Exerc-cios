soma = 0
print('¬' * 15)
print('Gerador de P.A.')
primeiro_t = int(input('Qual o primeiro termo da PA?: '))
razao = int(input('Qual a razão da PA?: '))
for c in range(1, 11):
    print(f'{primeiro_t + soma}', end=' > ')
    soma += razao
print('ACABOU')
