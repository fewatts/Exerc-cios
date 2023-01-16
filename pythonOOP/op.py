class Conta:
    def __init__(self, número, titular, saldo, limite):
        print('Iniciando nova conta...')
        self.número = número
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


    def cria_conta(número, titular, saldo, limite):
        conta = {'Número': número, 'Titular': titular, 
                'Saldo': saldo, 'Limite': limite}
        return conta


    def deposita(conta, valor):
        conta['Saldo'] += valor


    def saca(conta, valor):
        conta['Saldo'] -= valor


    def extrato(conta):
        num = conta['Número']
        saldo = conta['Saldo']
        print(f'Número: {num}\nSaldo: {saldo}')
