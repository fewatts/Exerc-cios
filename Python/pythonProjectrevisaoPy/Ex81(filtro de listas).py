lista = []
while True:
    num = int(input('Digite um número: [666 para parar] '))
    if num == 666:
        break
    else:
        lista.append(num)
tot = len(lista)
print('¬' * 40)
print(f'No total foram digitados {tot} valores')
lista.sort(reverse = True)
print(f'Lista decrescente: {lista}')
if 5 in lista:
    print('O valor 5 se encontra na lista!')
else:
    print('O valor 5 não se encontra na lista')
