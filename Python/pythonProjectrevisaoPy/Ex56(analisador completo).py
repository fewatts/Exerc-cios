soma_idade = 0
maior = 0
menor = 0
mulheres_menores = 0
nome_mais_velho = ''
opcao = ''
while opcao != 'N':
    for p in range(1, 5):
        print(f'¬¬¬¬¬¬ {p}ª pessoa ¬¬¬¬¬¬¬')
        nome = str(input('Nome? ')).strip()
        idade = int(input('Idade? '))
        sexo = str(input('Sexo? [M/F] ')).strip()
        soma_idade += idade
        if sexo in 'fF' and idade < 20:
            mulheres_menores += 1
        if p == 1 and sexo in 'Mm':
            maior = idade
            menor = idade
        else:
            if idade > maior and sexo in 'Mm':
                maior = idade
                nome_mais_velho = nome
            if idade < menor:
                menor = idade
    opcao = str(input('Deseja continuar? [S/N] ')).upper()
print(f'A média de idade do grupo é de {soma_idade / 4}')
print(f'No total são {mulheres_menores} mulheres com menos de 20 anos')
print(f'O mais velho tem {maior} anos e seu nome é {nome_mais_velho}')
