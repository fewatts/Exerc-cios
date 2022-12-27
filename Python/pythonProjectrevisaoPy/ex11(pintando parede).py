larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
print(f'''A sua parede tem as dimensões de {larg}X{alt}, sendo a área de {larg * alt} metros quadrados
Será necessário {(area * 1) / 2} litros de tinta para pintar a mesma.''')
