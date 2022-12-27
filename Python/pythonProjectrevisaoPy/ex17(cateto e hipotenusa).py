from math import hypot
cato = float(input('Qual o valor do cateto oposto? '))
cata = float(input('Qual o valor do cateto adjascente? '))
hip = hypot(cata, cato)
print(f'A hipotenusa vai medir {hip:.2f}')
