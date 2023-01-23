from Library.classes import *
contas = []


def títulos(msg):
    tam = len(msg) + 10
    print('~' * tam)
    print(f'     {msg}')
    print('¬' * tam)


def menu():
    print(f'''1-Criar contas
2-Mostrar Contas
3-Depositar 
4-Sacar
5-Fechar sistema''')


def criar_contas():
    qnt = int(input('Quantas contas deseja criar? '))
    for i in range(0, qnt):
        while True:
            n = str(input(f'Número da {i + 1}º conta: '))
            t = str(input('Titular: '))
            s = float(input('Saldo: '))
            l = float(input('Limite: '))
            print()
            print(f'Número: {n}\nTitular: {t}\nSaldo: {s}\nLimite: {l}')
            print()
            resp = str(input('Confirma os dados? [S/N] ')).strip().upper()[0]
            print()
            if resp in 'S':
                break
        conta = Conta.cria_conta(n, t, s, l)
        contas.append(conta)
    print()


def mostrar_contas():
    count = 0
    for c in contas:
        count += 1
        títulos(f'Banco WATTs Conta Nº{count}')
        for k, v in c.items():
            print(f'{k:<19}{v:>12}')
    print()


def processamento():
    while True:
        print()
        op = int(input('>>>> Sua opção: '))
        print()
        if op == 1:
            criar_contas()
            títulos('ESCOLHA')
            menu()
        elif op == 2:
           mostrar_contas()
           títulos('ESCOLHA')
           menu()
        elif op == 3:
            c = int(input('Digite o número da conta que deseja depositar: '))
            c -= 1
            if c >= len(contas):
                print('Número inválido...')
            v = float(input('Digite O valor de depósito: '))
            Conta.deposita(contas[c], v)
            títulos('ESCOLHA')
            menu()
        elif op == 4:
            c = int(input('Digite o número da conta que deseja depositar: '))
            c -= 1
            if c > len(contas):
                print('Número inválido...')
            v = float(input('Digite O valor de saque: '))
            Conta.saca(contas[c], v)
            títulos('ESCOLHA')
            menu()
        elif op == 5:
            break 
