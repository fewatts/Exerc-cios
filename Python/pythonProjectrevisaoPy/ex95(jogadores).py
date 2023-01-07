dados = {}
gols_ = []
jogadores = []
tot = 0
while True:
    dados['nome'] = str(input('Nome do jogador: '))
    dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for i in range(0, dados['partidas']):
        gol = int(input(f'Quandos gols na {i + 1} partida? '))
        tot += gol
        gols_.append(gol)
    dados['gols'] = gols_.copy()
    dados['total'] = tot
    jogadores.append(dados.copy())
    dados.clear()
    while True:
        resp = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break
print('_' * 40)
print(f'{"Nº":>3}  {"nome":>3}   {"Gols":<7}{"total":<}')
print('_' * 20)
