soma = 0
print('¬' * 10)
print('NMR. PRIMO')
numero = int(input('Digite um número: '))
for c in range(1, numero + 1):
    if numero % c == 0:
        print(f'\033[33m{c}\033[m', end=' ')
        soma += 1
    else:
        print(c, end=' ')
if soma == 2:
    print('\nO número é primo!')
else:
    print('\nO número não é primo...')
