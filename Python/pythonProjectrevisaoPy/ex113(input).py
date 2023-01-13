def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('...404... Digite um número válido!')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar o número...')
            return 0
        else:
            return n
    

def leiafloat(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('...404... Digite um número válido!')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar o número...')
            return 0
        else:
            return n    


#__Main__{
n = leiaint('Digite um número inteiro: ')
n1 = leiafloat('Digite um número real: ')
# }