def logo(msg):
    print(f'{msg:^20}')
    print('¬' * 20)


def area(larg, comp):
    area = larg * comp
    print(f'A área do terreno {larg:.1f}x{comp:.1f} é de {area:.1f}m2')

#__Main__:
logo('Área de terrenos')
largura = float(input('Largura [m]: '))
comprimento = float(input('Comprimento [m]: '))
area(largura, comprimento)
