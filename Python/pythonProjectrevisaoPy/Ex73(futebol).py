from numpy import sort
tabela = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians',
    'Athletico-PR', 'Athletico-MG', 'Botafogo', 'São paulo','América-MG', 'Fortaleza',
    'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Ceará', 'Athletico-GO', 
    'Cuiabá', 'Avaí', 'Juventude')
print('¬' * 30)
n = 1
print('Os 5 primeiros colocados:')
for i in tabela[0:5]:
    print(f'{n}ª {i}')
    n += 1
print('¬' * 30)
print('Os 4 últimos colocados:')
n = 17
for i in tabela[-4:]:
    print(f'{n}ª {i}')
    n += 1
print('¬' * 30)
print('Os times em ordem alfabética:')
for i in sort(tabela):
    print(i)
print('¬' * 30)
print(f'O São paulo está na {tabela.index("São paulo") + 1}ª posição.')
print('¬' * 30)
