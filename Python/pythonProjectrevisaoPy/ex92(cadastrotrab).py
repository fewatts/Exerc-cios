from datetime import date
pessoa = {}
atual = date.today().year
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = atual - nasc
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] == 0:
    print('¬' * 40)
    for k, v in pessoa.items():
        print(f'¬{k} tem o valor {v}')
else:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: '))
    print('¬' * 40)
    pessoa['aposentadoria'] = pessoa['contratação'] + 35
    for k, v in pessoa.items():
        print(f'¬{k} tem o valor de {v}')
