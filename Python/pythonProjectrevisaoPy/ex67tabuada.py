count = 0
print('¬' * 20)
print(' Tabuada while True ')
while True: 
    n = int(input('Digite um número para obter sua tabuada [Digite um número negativo para encerrar o programa]: '))
    print('¬' * 20)
    if n < 0:
        break
    while count != 11:
        print(f'{n} x {count} = {n * count}')
        count += 1
    print('¬' * 20)
    count = 0
print('Obrigado, volte sempre!')
print('END')
