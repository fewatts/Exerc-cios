viagem = float(input('Qual a distância da viagem? km '))
if viagem < 200:
    print(f'O custo da sua viagem vai ser de {(viagem * 0.5):.2f} R$')
else:
    print(f'O custo da sua viagem com desconto promocional vai ser de {(viagem * 0.45):.2f} R$')
    