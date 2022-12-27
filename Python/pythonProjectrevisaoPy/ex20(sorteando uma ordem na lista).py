from random import shuffle
lista = []
for c in range(1, 5):
    lista.append(input(f'{c}ª aluno: '))
shuffle(lista)
print(f'\033[7m A ordem de apresentação será: \033[m')
print(lista)
