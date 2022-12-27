número = 0
entradas = 0
soma_entradas = 0
while True:
    número = int(input('Digite números inteiros: [999 Para parar] '))
    if número == 999:
        break
    entradas += 1
    soma_entradas += número
print(f'No total foram {entradas} valores input e a soma deles é {soma_entradas}')
