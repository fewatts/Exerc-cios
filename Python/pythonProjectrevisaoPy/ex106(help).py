color = (
    '\033[m', #0-sem cor
    '\033[0;30;41m', #1-vermelho
    '\033[0;30;42m', #2-verde
    '\033[0;30;43m', #3-amarelo
    '\033[0;30;44m', #4-azul
    '\033[0;30;45m', #5-roxo
    '\033[0;30;46m'   #6-branco
)


def ajuda(msg):
    print(f'Acessando manual do comando {msg}')
    help(msg)
    

def título(tit, Color=0):
    tam = len(tit) + 4
    print(color[Color], end='')
    print('~' * tam)
    print(f'  {tit}  ')
    print('~' * tam)
    print(color[0], end='')
    


#__Main__{
título('Sistema interativo PyHelp', 4)
while True:
    print(color[4], end='')
    op = str(input('Digite uma função ou biblioteca do python \npara obter ajuda: [FIM para parar ou MOSTRAR para ver comandos] '))
    print(color[0], end='')
    if op.upper().strip() in 'FIM':
        break
    else:
        ajuda(op)
título('Obrigado e volte sempre!', 1)
# }