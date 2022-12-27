from random import randint
sorteio = (randint(1, 20), randint(1, 20), randint(1, 20),
           randint(1, 20), randint(1, 20))
print(f'Os números sorteados foram: {sorteio}')
print(f'O maior valor é {max(sorteio)}')
print(f'O menor valor é {min(sorteio)}')
