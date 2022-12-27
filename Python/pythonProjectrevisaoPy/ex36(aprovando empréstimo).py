print('¬' * 29)
print('Empréstimos imobiliários LTDA')
print('¬' * 29)
opcao = 0
while opcao != 777:
    casa = float(input('Qual o valor da casa? R$'))
    salario = float(input('Qual o seu salário mensal? R$'))
    anos = int(input('Em quantos anos o senhor quer financiar?:  '))
    parcela = (casa / (anos * 12))
    salario_min = salario * 0.3
    if salario_min >= parcela:
        print('Empréstimo liberado!')
    else:
        print('Empréstimo negado... renegocie seus valores!')
    print(f'Para pagar uma casa de R$ {casa} em {anos} a prestação será de {parcela:.2f}')
    opcao = int(input('Deseja continuar? 777 para parar: '))
