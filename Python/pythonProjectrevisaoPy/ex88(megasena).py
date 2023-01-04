from random import randint
from time import sleep
palpite = []
opção = 0
opção = int(input('Digite o número de jogos para sortear: '))
print('Sorteando...')
for i in range (0, opção):
    for p in range(0, 6):
        num = randint(1, 60)
        if num not in palpite:
            palpite.append(num)
        palpite.sort()
    sleep(1)
    print(f'Jogo nº{i + 1}: {palpite}')
    palpite.clear()
