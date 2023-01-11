from time import sleep
def linha():
    print('¬' * 60)


def count_pers(i, f, p):
    linha()
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    if f > 0:
        print(f'Contando de {i} até {f} de {p} em {p}')
        for i in range(i, f, p):
            sleep(0.5)
            print(f'{i}', end=' ')
        print('FIM...')
        print()
    else:
        print(f'Contando de {i} até {f} de {p} em {p}')
        for i in range(i, f + 1, -p):
            sleep(0.5)
            print(f'{i}', end=' ')
        print('FIM...')
        print()


#__main__:
count_pers(1, 10, 1)
count_pers(10, 0, 2)
print('Sua vez de escolher um contador: ')
início = int(input('Início: '))
fim = int(input('Fim: '))
pulo = int(input('Passo: '))
count_pers(início, fim, pulo)
