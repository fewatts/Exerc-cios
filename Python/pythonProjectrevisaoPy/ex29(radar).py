vel = float(input('Qual a velocidade do carro? Km/h '))
if vel > 80:
    print(f'\033[31mInfelizmente você foi multado\033[m')
    print(f'\033[31mO senhor/a deverá pagar {((vel - 80) * 7):.0f} R$\033[m')
else:
    print('Tudo certo! Dirija com atenção meu querido/a')
