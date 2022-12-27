frase = str(input('Digite uma frase: ')).strip().upper()
separado = frase.split()
junto = ''.join(separado)
inverso = junto[:: -1]
if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo...')
print(f'Você digitou a frase {junto} e o inverso dela é {inverso}')
