def menu():
    print('#' * 50)
    print(f'{"MENU PRINCIPAL":^50}')
    print('¬' * 50)
    print('''1- Ver pessoas cadastradas
2-Cadastrar uma nova pessoa
3-Sair do sistema''')
    print('¬' * 50)


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('O valor digitado não é válido...')
            continue
        except KeyboardInterrupt:
            print('O usuário interrompeu o funcionamento do programa...')
            return 0
        else:
            return n


def opção_1():
    print('~' * 50)
    print(f'{"PESSOAS CADASTRADAS":^50}')
    print('¬' * 50)


def opção_2():
    print('=' * 50)
    print(f'{"CADASTRAR NOVA PESSOA":^50}')
    print('¬' * 50)


def opção_3():
    print('*' * 50)
    print(f'{"FECHANDO PROGRAMA":^50}')
    print('¬' * 50)
