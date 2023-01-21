class Conta:
    def __init__(self, número, titular, saldo, limite):
        self.número = número
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    

    def cria_conta(numero, titular, saldo, limite):
        conta = {'Número': numero, 'Titular': titular, 'Saldo': saldo, 'Limite': limite}
        return conta
    

    def deposita(conta, valor):
        conta['Saldo'] += valor


    def saca(conta, valor):
        if conta['Saldo'] >= valor:
            conta['Saldo'] -= valor
        else:
            print('Saldo insuficiente...')


    def get_titular(conta):
        return conta['Titular']
