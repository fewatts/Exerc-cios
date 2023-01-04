from random import randint
from time import sleep
print('¬' * 40)
print(f'{"MEGA-SENA":^40}')
print('¬' * 40)
palpite = []
palp_tot = []
opção = 0
opção = int(input('Digite o número de jogos para sortear: '))
print('Sorteando...')
for i in range (0, opção):
    for p in range(0, 6):
        num = randint(1, 60)
        if num not in palpite:
            palpite.append(num)
    palpite.sort()
    palp_tot.append(palpite[:])
    palpite.clear()
print('¬' * 40)
print(f'{"PALPITES":^40}')
print('¬' * 40)
for i, ps in enumerate(palp_tot):
    sleep(0.5)
    print(f'Jogo {i + 1}: {ps}')
    print()
