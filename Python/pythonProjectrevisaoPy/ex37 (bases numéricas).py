while True:
    n = int(input('Digite um número inteiro: '))
    option = int(input('''Qual a opção de conversão?
    [1] binário
    [2] octal
    [3] hexadecimal
    Sua opção (Digite qualquer outro número para parar): '''))
    if option == 1:
        print(f'Binário: {bin(n)[2:]}')
    elif option == 2:
        print(f'octal: {oct(n)[2:]}')
    elif option == 3:
        print(f'hexadecimal: {hex(n)[2:]}')
    else:
        print('Obrigado por utilizar meu algorítimo!!')
        break
