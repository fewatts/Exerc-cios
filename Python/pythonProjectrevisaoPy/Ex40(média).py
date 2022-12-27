a = float(input('Digite a Primeira nota: '))
b = float(input('Digite a Segunda nota: '))
c = float(input('Digite a Terceira nota: '))
média = (a + b + c) / 3
if média < 5:
    print('Você infelizmente foi \033[33mreprovado\033[m...')
if 5 < média < 7:
    print('Você está de \033[33mrecuperação\033[m...')
else:
    print('Você foi \033[36maprovado\033[m! parabéns! ')
