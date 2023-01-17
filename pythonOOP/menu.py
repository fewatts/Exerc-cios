from classes import *

def títulos(msg):
    tam = len(msg) + 10
    print('~' * tam)
    print(f'     {msg}')
    print('¬' * tam)


def menu():
    print(f'''1-Criar conta
2-Verificar extrato
3-Depositar
4-Sacar
5-Transferir
6-Fechar sistema
''')


def criar_cliente():
    try:
        while True:
            dados = []
            dados.clear()
            dados.append(str(input('Nome: ')))
            dados.append(str(input('Sobrenome: ')))
            dados.append(str(input('CPF: ')))
            for d in dados:
                print(f'{d}...', end='')
            resp = str(input('\nConfirma os dados? [S/N] ')).strip().upper()[0]
            if resp in 'S':
                cliente_0 = Cliente(dados[0], dados[1], dados[2])
                print('Dados Adicionados!')
                return cliente_0
    except:
        print('ERRO...')

def criar_conta(cliente):
    try:
        while True:
            dados = []
            dados.clear()
            dados.append(str(input('Nº da conta: ')))
            dados.append(cliente.nome)
            dados.append(float(input('SALDO: ')))
            dados.append(float(input('LIMITE: ')))
            for d in dados:
                print(f'{d}...', end='')
            resp = str(input('\nConfirma os dados? [S/N] ')).strip().upper()[0]
            if resp in 'S':
                conta_0 = Conta(dados[0], cliente, dados[2], dados[3])
                print('Dados Adicionados!')
                print(conta_0.número)
                print(conta_0.cliente)
                print(conta_0.saldo)
                print(conta_0.limite)
                return conta_0
    except:
        print('ERRO...')
