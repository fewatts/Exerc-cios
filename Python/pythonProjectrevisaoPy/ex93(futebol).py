dados = {}
gols_ = []
tot = 0
dados['nome'] = str(input('Nome do jogador: '))
dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for i in range(0, dados['partidas']):
    gol = int(input(f'Quandos gols na {i + 1} partida? '))
    tot += gol
    gols_.append(gol)
dados['gols'] = gols_.copy()
dados['total'] = tot
print('¬' * 50)
print(dados)
print('¬' * 50)
for k, v in dados.items():
    print(f'O campo {k} tem valor de {v}')
print('¬' * 50)
print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas')
for i, v in enumerate(dados['gols']):
    print(f'   >>>Na partida {i + 1} o jogador fez {v} gols')
print(f'No total foram {tot} gols')
