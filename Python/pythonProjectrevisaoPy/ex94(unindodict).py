soma_id = média = 0
pessoa = {}
pessoas = []
mulheres = []
acima_med = []
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper().strip()[0]
        if pessoa['sexo'] in 'F':
            mulheres.append(pessoa['nome'])
        if pessoa['sexo'] in 'MF':
            break
        print('404! Digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma_id += pessoa['idade']
    pessoa.copy()
    pessoas.append(pessoa.copy())
    pessoa.clear()
    resp = str(input('Deseja continuar? ')).upper().strip()[0]
    if resp in 'N':
        break
print('¬' * 40)
média = soma_id / len(pessoas)
print(f'A) No total foram {len(pessoas)} pessoas cadastradas')
print(f'B) A média das idades é igual a {média:.2f}')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in mulheres:
    print(f'{p}...', end='')
print()
print('D) As pessoas com idade acima da média são: ', end='')
for p in pessoas:
    if p['idade'] > média:
        print(f'{p["nome"]}...', end='')
