sexo = ''
sexo = str(input('Informe seu sexo: [M/F] ')).upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos, informe seu sexo: [M/F] ')).upper()
if sexo == 'M' or sexo == 'F':
    print(f'Sexo {sexo} registrado com sucesso')
