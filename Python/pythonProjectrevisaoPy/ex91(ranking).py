from random import randint
from time import sleep
from operator import itemgetter
jogadores = {
    'jogador_1': randint(1, 10),
    'jogador_2': randint(1, 10),
    'jogador_3': randint(1, 10),
    'jogador_4': randint(1, 10),
    'jogador_5': randint(1, 10),
    'jogador_6': randint(1, 10),
    'jogador_7': randint(1, 10),
    'jogador_8': randint(1, 10),
    'jogador_9': randint(1, 10),
    'jogador_10': randint(1, 10)
}
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for k, v in jogadores.items():
    print(f'O {k} jogou: {v}')
print('¬' * 40)
for i, v in enumerate(rank):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
