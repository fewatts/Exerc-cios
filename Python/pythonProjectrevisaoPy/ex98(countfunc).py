from time import sleep
def linha():
    print('¬' * 60)


def intro():
    linha()
    print('Contando de 1 até 10 de 1 em 1:')
    for i in range(1, 11, 1):
        sleep(0.5)
        print(f'{i}', end=' ')
    print('FIM...')
    print()
    linha()
    print('Contagem de 10 até 0 pulando de 2 em 2')
    for i in range(10, 0, -2):
        sleep(0.5)
        print(f'{i}', end=' ')
    print('FIM...')
    print()


def count_pers(i, f, p):
    linha()
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    if f > 0:
        print(f'Contando de {i} até {f} de {p} em {p}')
        for i in range(i, f + 1, p):
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
intro()
print('Sua vez de escolher um contador: ')
início = int(input('Início: '))
fim = int(input('Fim: '))
pulo = int(input('Passo: '))
count_pers(início, fim, pulo)
