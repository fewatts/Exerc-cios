from datetime import date
maiores = 0
menores = 0
atual = date.today().year
for c in range(1, 8):
    ano_de_nascimento = int(input('Qual seu ano de nascimento? '))
    idade = atual - ano_de_nascimento
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print(f'No total são {maiores} maiores de idade e \n{menores} menores de idade.')
