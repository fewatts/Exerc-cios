from datetime import date
ano_de_nascimento = int(input('Qual o ano de nascimento do nadador? '))
atual = date.today().year
idade = atual - ano_de_nascimento
if idade <= 9:
    print('Este nadador é MIRIM')
elif idade <= 14:
    print('Este nadador é INFANTIL')
elif idade <= 19:
    print('Este nadador é JUNIOR')
elif idade <= 25:
    print('Este nadador é SÊNIOR')
else:
    print('Este nadador é MASTER!')
