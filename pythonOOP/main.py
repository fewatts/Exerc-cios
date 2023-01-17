from menu import *
from classes import *

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
            print(cliente_0)
            print(conta_0)        
títulos('Volte sempre!')
