def logo():
    print(f'{msg:^10}')
    print('¬' * 10)


def area(larg, comp):
    area = larg * comp
    return area


#__Main__
largura = float(input('Largura [m]: '))
comprimento = float(input('Comprimento [m]: '))
area(largura, comprimento)
print(f'A área do terreno {largura.:1f}x{comprimento.:1f} é de {area.:1f}m2')
