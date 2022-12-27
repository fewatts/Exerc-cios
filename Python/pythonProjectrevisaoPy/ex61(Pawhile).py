soma = 0
termos = 0
print('¬' * 15)
print('Gerador de P.A.')
primeiro_t = int(input('Qual o primeiro termo da PA?: '))
razao = int(input('Qual a razão da PA?: '))
while termos != 10:
    termos += 1
    print(f'{primeiro_t + soma}', end=' > ')
    soma += razao
print('ACABOU')
