from random import choice
lista = []
for c in range(1, 5):
    lista.append(input(f'{c}ª aluno: '))
print(f'\033[7m O escolhido foi {choice(lista)} \033[m')
