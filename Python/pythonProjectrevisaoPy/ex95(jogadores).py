gols = []
jogador = {}
jogadores = []
#OK
while True:
    tot = 0
    gols.clear()
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(0, jogador['partidas']):
        gols_ = int(input(f'  Quantos gols fez na {p + 1} partida? '))
        gols.append(gols_)
        tot += gols_
    jogador['total'] = tot
    jogador['gols'] = gols.copy()
    jogadores.append(jogador.copy())
    while True:
        resp = str(input('   Continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('...404... S ou N!')
    if resp in 'N':
        break
#OK
print('#' * 70)
print('Nº', end=' ')
for i in jogador.keys():
    print(f'{i:>15}', end='')
print()
#OK
print('¬' * 70)
for i, j in enumerate(jogadores):
    print(f'{i:>1}', end='')
    for v in j.values():
        print(f'{str(v):>16}', end='')
    print()
#OK
while True:
    print('¬' * 70)
    bus = int(input('Deseja ver dados de qual jogador? [9999 para parar] '))
    if bus == 9999:
        break
    if bus >= len(jogadores):
        print('...404... Esse número não está contido na lista!')
    else:
        print(f'~~~~ Dados do jogador {jogadores[bus]["nome"]}')
        for i, v in enumerate(jogadores[bus]['gols']):
            print(f'Na {i + 1} partida o jogador fez {v} gols...')
print('¬¬¬¬ Obrigado pelo uso!')
#OK
