class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
        
    def deposita(self, valor):
        self.saldo += valor
    

    def saca(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False
    

    def transfere(self, destino, valor):
        retirou = self.saca(valor)
        if retirou == False:
            return False
        else:
            return True


    def extrato(self):
        print(f'Titular: {self.titular}\nSaldo: {self.saldo}')


conta_0 = Conta('123-4', 'joão', 1723.24, 5400.0)
conta_1 = Conta('234-5', 'fernando', 1895.34, 5000)

conta_0.deposita(50)
conta_1.saca(2000)

conta_0.extrato()
conta_1.extrato()
