from random import randint
acho = ''
senha = input('Senha: ')
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
          'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
          'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
          'Y', 'Z']
while acho != senha:
    acho = ''
    for letra in senha:
        acholetra = letras[randint(0, 52)]
        acho = str(acholetra) + str(acho)
    print(acho)
print(f'A senha encontrada foi: {acho}')
