pessoa = []
menor = maior = 0
lista_nome_peso = []
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso [KG]: ')))
    if len(lista_nome_peso) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    lista_nome_peso.append(pessoa[:])
    pessoa.clear()
    opção = str(input('Deseja continuar? [S/N]  ')).upper().strip()[0]
    if opção in 'N':
        break
print('¬' * 60)
print(f'No total foram {len(lista_nome_peso)} pessoas cadastradas')
print(f'O maior peso foi {maior}', end='')
for p in lista_nome_peso:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {menor}',end='')
for p in lista_nome_peso:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
