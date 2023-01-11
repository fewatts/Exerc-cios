def ficha(n='<UNKNOWN>', g=0):
    print(f'O jogador {n} fez {g} gol/s!')


#__main__{
nome = str(input('Nome do jogador: '))
gols = str(input('Gols: '))
if gols.isnumeric():
    g = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g = gols)
else:
    ficha(nome, gols)
# }