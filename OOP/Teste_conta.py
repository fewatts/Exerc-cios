class Conta:
    def __init__(self, número, titular, saldo, limite):
        print('Iniciando conta...')
        self.número = número
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    

    def cria_conta(numero, titular, saldo, limite):
        conta = {'Número': numero, 'Titular': titular, 'Saldo': saldo, 'Limite': limite}
        return conta
    

    def deposita(conta, valor):
        conta['Saldo'] += valor


    def get_titular(conta):
        return conta['Titular']


def títulos(msg):
    tam = len(msg) + 10
    print('~' * tam)
    print(f'     {msg}')
    print('¬' * tam)


títulos('BANCO WATTs')
contas = []
qnt = int(input('Quantas contas deseja criar? '))
for i in range(0, qnt):
    while True:
        n = str(input(f'Número da {i + 1}º conta: '))
        t = str(input('Titular: '))
        s = float(input('Saldo: '))
        l = float(input('Limite: '))
        resp = str(input('Confirma os dados? [S/N] ')).strip().upper()[0]
        if resp in 'S':
            break
    conta = Conta.cria_conta(n, t, s, l)
    contas.append(conta)
    print()
count = 1
for c in contas:
    títulos(f'Banco WATTs Conta Nº{count}')
    for k, v in c.items():
        print(f'{k:<16}{v:>12}')
    print()
    count += 1
