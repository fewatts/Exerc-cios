dia = int(input('Quantos dias o carro foi usado? '))
km = float(input('Quantos kilometros foram rodados? '))
print(f'O preço a pagar pelo serviço é {(dia * 60) + (km * 0.15):.2f} R$')
