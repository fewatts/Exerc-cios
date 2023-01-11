from random import randint
from time import sleep
números = []

#DEF OK
def sorteia():
    for i in range(0, 5):
        n = 0
        n = randint(1, 10)
        números.append(n)
    print(f'Sorteados: ', end='')
    for i in números:
        sleep(0.3)
        print(f'{i}...', end='')
    

#DEF OK
def somapar():
    soma = 0
    print()
    print('Números pares: ', end='')
    for v in números:
        if v % 2 == 0:
            soma += v
            sleep(0.3)
            print(f'{v}...', end='')
    print()
    print(f'A soma dos valores Pares foi de {soma}')
    print()


#__main__{
sorteia()
somapar()
#}