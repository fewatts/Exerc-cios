import datetime  

class Histórico:

    __slots__ = ['__data_abertura', '__transações']

    def __init__(self):
        try:
            self.__data_abertura = datetime.datetime.today()
            self.__transações = []
        except:
            print('ERRO...')


    def imprime(self):
        try:
            print(f'Data de abertura: {self.__data_abertura}')
            print('Transações: ')
            for t in self.__transações:
                print('-', t)
        except:
            print('ERRO...')


class Cliente:
        
    __slots__ = ['__nome', '__sobrenome', '__cpf']

    def __init__(self, nome, sobrenome, cpf):
        try:
            self.__nome = nome
            self.__sobrenome = sobrenome
            self.__cpf = cpf
        except:
            print('ERRO...')    


class Conta:

    __slots__ = ['__número', '__titular', '__saldo', '__limite']

    def __init__(self, número, cliente, saldo=0.0, limite=500):
        try:
            print('Iniciando nova conta...')
            self.__número = número
            self.__titular = cliente
            self.__saldo = saldo
            self.__limite = limite
            self.__histórico = Histórico()
            Conta.__tot_contas += 1
        except:
            print('ERRO...')


    def get__saldo(self):
        try:
            return self.__saldo
        except:
            print('ERRO...')


    def set__saldo(self, saldo):
        try:
            if saldo < 0:
                print('O saldo não pode ser negativo!')
            else:
                self.__saldo = saldo
        except:
            print('ERRO...')


    @classmethod
    def get__tot_contas():
        try:
            return Conta.__tot_contas
        except:
            print('ERRO...')


    def get__titular(self):
        try:
            return self.__titular
        except:
            print('ERRO...')
    

    def set__titular(self, titular):
        try:
            self.__titular = titular
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
        self.__saldo += valor
        self.__histórico.__transações.append(f'Depósito de {valor}')


    def saca(self, valor):
        try:
            if (self.__saldo < valor):
                return False
            else:
                self.__saldo -= valor
                self.__histórico.__transações.append(f'Saque de {valor}')
                return True
        except:
            print('ERRO...')


    def extrato(self):
        try:
            print(f'Número: {self.__número}\nSaldo: {self.__saldo}')
            self.__histórico.__transações.append(f'Tirou extrato - saldo de {self.__saldo}')
        except:
            print('ERRO...')


    def transfere_para(self, destino, valor):
        try:
            retirou = self._saca(valor)
            if (retirou == False):
                return False
            else:
                destino.deposita(valor)
                self.__histórico.__transações.append(f'Transferência de {valor} para a conta {destino.número}')
                return True
        except:
            print('ERRO...')


contas = []


def criar_contas():
    qnt = int(input('Quantas contas deseja criar? '))
    for i in range(0, qnt):
        while True:
            nom = str(input('1º Nome: '))
            sob = str(input('Sobrenome: '))
            cpf = str(input('CPF: '))
            n = str(input(f'Número da conta de {nom}: '))
            t = nom
            s = float(input('Saldo: '))
            l = float(input('Limite: '))
            print()
            print(f'Nome: {nom}\nSobrenome: {sob}\nCFP: {cpf}\nNúmero: {n}\nTitular: {t}\nSaldo: {s}\nLimite: {l}')
            print()
            resp = str(input('Confirma os dados? [S/N] ')).strip().upper()[0]
            print()
            if resp in 'S':
                break
        conta_ = Cliente(nom, sob, cpf)
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
            while True:
                c = int(input('Digite o número da conta que deseja depositar: '))
                c -= 1
                if c > len(contas):
                    print('Número inválido...')
                else:
                    break
            v = float(input('Digite O valor de depósito: '))
            Conta.deposita(contas[c], v)
            títulos('ESCOLHA')
            menu()
        elif op == 4:
            while True:
                c = int(input('Digite o número da conta que deseja sacar: '))
                c -= 1
                if c > len(contas):
                    print('Número inválido...')
                else:
                    break
            if c > len(contas):
                print('Número inválido...')
            v = float(input('Digite O valor de saque: '))
            Conta.saca(contas[c], v)
            títulos('ESCOLHA')
            menu()
        elif op == 5:
            while True:
                c = int(input('Digite o número da conta que deseja ver o histórico: '))
                c -= 1
                if c > len(contas):
                        print('Número inválido...')
                else:
                    break
            Conta.extrato(contas[c])
            títulos('ESCOLHA')
            menu()
        elif op == 6:
            break
        else:
            print('Opção inválida...') 


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
5-Histórico das contas
6-Fechar sistema''')
