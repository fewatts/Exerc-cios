lista = []
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado não pode ser adicionado')
    else:
        print('Valor adicionado!')
        lista.append(n)
    option = str(input('Deseja continuar? [S/N]  ')).upper().strip()[0]
    if option in 'N':
        break
lista.sort()
print('¬' * 30)
print(f'O valores digitados foram: {lista}')
