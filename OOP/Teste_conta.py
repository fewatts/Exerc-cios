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


contas = []
qnt = int(input('Quantas contas deseja criar? '))
for i in range(0, qnt):
    n = str(input(f'Número da {i + 1}º conta: '))
    t = str(input('Titular: '))
    s = float(input('Saldo: '))
    l = float(input('Limite: '))
    conta = Conta.cria_conta(n, t, s, l)
    contas.append(conta)
    print()
print(contas)
