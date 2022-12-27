from time import sleep
from random import randint
print('¬' * 53)
print('Vou pensar em um número entre 0 e 10, Tente adivinhar! ')
print('¬' * 53)
count = 0
computador = randint(0, 10)
while True:
    jogador = int(input('Tente adivinhar o número!: '))
    count += 1
    print('PROCESSANDO...')
    sleep(2)
    if jogador == computador:
        print(f'Eu joguei {computador} e você jogou {jogador}, você me venceu!!')
        break
    else:
        print('Eu te venci!!')
        if jogador > computador:
            print('O número que eu pensei é menor!')
        else:
            print('O número que eu pensei é maior!')
print(f'No total foram {count} jogadas até você me vencer!')
