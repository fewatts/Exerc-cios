a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
if a > b:
   print(f'O maior valor é {a} e o menor é o {b}')
elif b > a:
    print(f'O maior valor é {b} e o menor valor é {a}')
else:
    print(f'Os valores {a} e {b} são iguais!')
