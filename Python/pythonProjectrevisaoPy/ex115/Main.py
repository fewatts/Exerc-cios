import Validaçãomenu
#__Main__{
while True:
    Validaçãomenu.menu()
    opção = Validaçãomenu.leiaint('>>> Sua opção: ')
    if opção == 1:
        Validaçãomenu.opção_1
    elif opção == 2:
        Validaçãomenu.opção_2
    elif opção == 3:
        print('Volte sempre!')
        break
    else:
        print('Opção inválida...')
# }