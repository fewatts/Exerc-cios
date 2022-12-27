from time import sleep
from random import randint
print('¬' * 53)
print('Vou pensar em um número entre 0 e 5, Tente adivinhar! ')
print('¬' * 53)
computador = randint(0, 5)
player = int(input('Qual número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if player == computador:
    print('Você me ganhou! Escolhemos os mesmos números!')
else:
    print(f'Infelismente, eu venci! HAHAHAHAHAHAHAHAHAHAAH\n eu escolhi {computador} e você  escolheu {player}')
