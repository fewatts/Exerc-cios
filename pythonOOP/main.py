from menu import *
from classes import *
contas = []

while True:
    títulos('ADM. BANCO WATTS')
    menu()
    op = int(input('>>>>> Opção: '))
    if op == 6:
        break
    else:
        if op == 1:
            cliente_0 = criar_cliente()
            conta_0 = criar_conta(cliente_0)
            print()
            contas.append(conta_0)
            print(f'Conta de {cliente_0.nome} criada com sucesso!\nnº {conta_0.número}')
títulos('Volte sempre!')
