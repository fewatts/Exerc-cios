numeros = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))
print(f'''Os números digitados foram: {numeros}
O número 9 foi digitado {numeros.count(9)} vezes''')
if 3 in numeros:
    print(f'O número 3 apareceu a primeira vez na {numeros.index(3) + 1}º posição')
else:
    print('O número 3 não foi digitado.')
for n in numeros:
    if n % 2 == 0:
        print(f'Os números pares foram {n}')
    