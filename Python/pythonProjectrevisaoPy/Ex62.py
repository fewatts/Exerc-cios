print('¬' * 15)
print('Gerador de P.A.')
primeiro = int(input('Qual o primeiro termo da PA?: '))
razao = int(input('Qual a razão da PA?: '))
soma = 0
termos = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while termos != total:
        termos += 1
        print(f'{primeiro + soma}', end=' > ')
        soma += razao
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? [0 para parar] '))
print(f'Foram no total {total} termos')
print('FIM')
