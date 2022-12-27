from random import randint
print(' Jogo do par ou ímpar ')
print('¬' * 22)
while True:
    jogador = int(input('Digite um valor: '))
    jogadorstr = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print('¬' * 22)
    computador = randint(0, 10)
    soma = jogador + computador
    print(f'Você digitou {jogador} e o computador escolheu {computador}. A soma é {jogador + computador}', end='')
    if soma % 2 == 0:
        print(' DEU PAR', end='')
        resultado = 'P'
    else:
        print(' DEU ÍMPAR', end='')
        resultado = 'I'
    if resultado == jogadorstr:
        print('\nVocê venceu!\nVamos jogar novamente...')
    else:
        print('\nVocê perdeu!\nGAME OVER!')
        break
print('END')
