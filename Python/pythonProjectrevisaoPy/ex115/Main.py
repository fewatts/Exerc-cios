from lib import Validaçãomenu
from lib import arquivo
arq = 'arquivo.txt'

#__Main__{
if not arquivo.arquivoexiste(arq):
    arquivo.criararquivo(arq)

while True:
    Validaçãomenu.menu()
    opção = Validaçãomenu.leiaint('>>> Sua opção: ')
    if opção == 1:
        Validaçãomenu.opção_1()
        arquivo.lerarquivo(arq)
    elif opção == 2:
        Validaçãomenu.opção_2()
        nome = str(input('Nome: '))
        idade = Validaçãomenu.leiaint('Idade: ')
        arquivo.editararquivo(arq, nome, idade)
    elif opção == 3:
        Validaçãomenu.opção_3()
        print('Volte sempre!')
        break
    else:
        print('Opção inválida...')
# }