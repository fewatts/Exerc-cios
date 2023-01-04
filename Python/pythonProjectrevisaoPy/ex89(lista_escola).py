lista = list()
while True:
    nome = str(input('Nome do aluno: '))
    nota_prova = float(input('Nota da prova: '))
    pim = float(input('Nota PIM: '))
    ava = float(input('Nota AVA: '))
    média = (((nota_prova * 7) + (pim * 2) + (ava)) / 10)
    lista.append([nome, [nota_prova, pim, ava], média])
    resp = str(input('Deseja continuar?  [S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
print('_' * 30)
print(f'{"Nº":<4}{"Nome":<10}{"Média":>8}')
for i, alu in enumerate(lista):
    print(f'{i:<4}{alu[0]:<10}{alu[2]:>8.2f}')
print('_' * 30)
print()
while True:
    Esc = int(input('Deseja ver notas de qual aluno?[999 p/ sair] '))
    if Esc == 999:
        break
    if Esc <= len(lista) - 1:
        print(f'As notas de {lista[Esc][0]} são {lista[Esc][1]}')
print('Fechando Programa..........')
