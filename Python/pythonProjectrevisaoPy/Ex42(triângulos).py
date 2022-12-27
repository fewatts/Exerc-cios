print('¬' * 24)
print('\033[35;44mAnalisador de triângulos\033[m')
print('¬' * 24)
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceito valor: '))
if a + b > c and a + c > b and b + c > a:
    print('É possível formar triângulo com o valor informado!')
    if a == b == c:
        print('Este triângulo é EQUILÁTERO')
    elif a == b or b == c or a == c:
        print('Este triângulo é ISÓCELES')
    elif a != b != c != a:
        print('Este triângulo é ESCALENO')
else:
    print('Não é possível formar triângulo...')
