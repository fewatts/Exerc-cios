def leiaint(n):
    while True:
        num = str(input(n))
        if num.isnumeric():
            num = int(num)
            break
        print('...404... Digite um número!')
    return num


#__main__{
número = leiaint('Digite um número: ')
print(f'Você digitou o número {número}')
# }