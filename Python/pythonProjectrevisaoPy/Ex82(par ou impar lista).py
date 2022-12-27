lista_num = []
lista_par = []
lista_imp = []
print('¬' * 30)
print(f'{"PAR OU ÍMPAR?":^30}')
print('¬' * 30)
while True:
    lista_num.append(int(input('Digite um número inteiro: ')))
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
for i in range(0, len(lista_num)):
    if lista_num[i] % 2 == 0:
        lista_par.append(lista_num[i])
    else:
        lista_imp.append(lista_num[i])
print(f'Números pares: {lista_par}')
print(f'Números ímpares: {lista_imp}')
