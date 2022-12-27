numbers = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
         'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
         'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True: 
    while True:
        number = int(input('Digite um número [De 0 a 20]: '))
        if 0 <= number <= 20:
            break
        print('Apenas números de 0 a 20!')
    print(f'O número digitado foi {numbers[number]}')
    option = str(input('Deseja começar novamente? [S/N] ')).strip().upper()[0]
    if option in 'N':
        break
print('Fim do programa!')
