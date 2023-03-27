import datetime  

class Histórico:

    __slots__ = ['_data_abertura', '_transações']

    def __init__(self):
        
        self._data_abertura = datetime.datetime.today()
        self._transações = []
    
        


    def imprime(self):
        
        print(f'Data de abertura: {self.data_abertura}')
        print('Transações: ')
        for t in self._transações:
            print('-', t)
    
        


class Cliente:
        
    __slots__ = ['_nome', '_sobrenome', '_cpf']

    def __init__(self, nome, sobrenome, cpf):
        
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
    
            


class Conta:

    __slots__ = ['_número', '_titular', '_saldo', '_limite']

    def __init__(self, número, cliente, saldo=0.0, limite=500):
        
        print('Iniciando nova conta...')
        self._número = número
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._histórico = Histórico()
        Conta._tot_contas += 1
    
        


    def get_saldo(self):
        
        return self._saldo
    
        


    def set_saldo(self, saldo):
        
        if saldo < 0:
            print('O saldo não pode ser negativo!')
        else:
            self._saldo = saldo
    
        


    @classmethod
    def get_tot_contas():
        
        return Conta._tot_contas
    
        


    def get_titular(self):
        
        return self._titular
    
        
    

    def set_titular(self, titular):
        
        self._titular = titular
    
        


    def cria_conta(número, titular, saldo, limite):
        
        conta = {'Número': número, 'Titular': titular, 
                'Saldo': saldo, 'Limite': limite}
        return conta
    
        


    def deposita(self, valor):
        
        self._saldo += valor
        self._histórico._transações.append(f'Depósito de {valor}')
    
        


    def saca(self, valor):
        
        if (self.saldo < valor):
            return False
        else:
            self._saldo -= valor
            self._histórico._transações.append(f'Saque de {valor}')
            return True
    
        


    def extrato(self):
        
        print(f'Número: {self._número}\nSaldo: {self._saldo}')
        self._histórico._transações.append(f'Tirou extrato - saldo de {self._saldo}')
    
        


    def transfere_para(self, destino, valor):
        
        retirou = self._saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self._histórico._transações.append(f'Transferência de {valor} para a conta {destino.número}')
            return True
    
        
