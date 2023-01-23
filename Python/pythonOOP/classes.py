import datetime  

class Histórico:

    __slots__ = ['_data_abertura', '_transações']

    def __init__(self):
        try:
            self._data_abertura = datetime.datetime.today()
            self._transações = []
        except:
            print('ERRO...')


    def imprime(self):
        try:
            print(f'Data de abertura: {self.data_abertura}')
            print('Transações: ')
            for t in self._transações:
                print('-', t)
        except:
            print('ERRO...')


class Cliente:
        
    __slots__ = ['_nome', '_sobrenome', '_cpf']

    def __init__(self, nome, sobrenome, cpf):
        try:
            self._nome = nome
            self._sobrenome = sobrenome
            self._cpf = cpf
        except:
            print('ERRO...')    


class Conta:

    __slots__ = ['_número', '_titular', '_saldo', '_limite']

    def __init__(self, número, cliente, saldo=0.0, limite=500):
        try:
            print('Iniciando nova conta...')
            self._número = número
            self._titular = cliente
            self._saldo = saldo
            self._limite = limite
            self._histórico = Histórico()
            Conta._tot_contas += 1
        except:
            print('ERRO...')


    def get_saldo(self):
        try:
            return self._saldo
        except:
            print('ERRO...')


    def set_saldo(self, saldo):
        try:
            if saldo < 0:
                print('O saldo não pode ser negativo!')
            else:
                self._saldo = saldo
        except:
            print('ERRO...')


    @classmethod
    def get_tot_contas():
        try:
            return Conta._tot_contas
        except:
            print('ERRO...')


    def get_titular(self):
        try:
            return self._titular
        except:
            print('ERRO...')
    

    def set_titular(self, titular):
        try:
            self._titular = titular
        except:
            print('ERRO...')


    def cria_conta(número, titular, saldo, limite):
        try:
            conta = {'Número': número, 'Titular': titular, 
                    'Saldo': saldo, 'Limite': limite}
            return conta
        except:
            print('ERRO...')


    def deposita(self, valor):
        try:
            self._saldo += valor
            self._histórico._transações.append(f'Depósito de {valor}')
        except:
            print('ERRO...')


    def saca(self, valor):
        try:
            if (self.saldo < valor):
                return False
            else:
                self._saldo -= valor
                self._histórico._transações.append(f'Saque de {valor}')
                return True
        except:
            print('ERRO...')


    def extrato(self):
        try:
            print(f'Número: {self._número}\nSaldo: {self._saldo}')
            self._histórico._transações.append(f'Tirou extrato - saldo de {self._saldo}')
        except:
            print('ERRO...')


    def transfere_para(self, destino, valor):
        try:
            retirou = self._saca(valor)
            if (retirou == False):
                return False
            else:
                destino.deposita(valor)
                self._histórico._transações.append(f'Transferência de {valor} para a conta {destino.número}')
                return True
        except:
            print('ERRO...')
