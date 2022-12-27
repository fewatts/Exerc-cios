#a = b[:] não cria conexão entre listas
#a = b cria conexão
from random import randint
count = 0
valores = []
while count <= 10:
    valores.append(randint(1, 10))
    count += 1
for var in range(0, 4):
    valores.append(int(input('Digite um valor int: ')))
for p, v in enumerate(valores):
    print(f'Achei o valor {v} na posição {p + 1}')
