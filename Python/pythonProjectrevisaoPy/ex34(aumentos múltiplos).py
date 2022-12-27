salario = float(input('Qual o salário do funcionário?: R$ '))
if salario > 1250:
    salario_final = (salario * 0.1) + salario
    print(f'O salário com aumento é o seguinte {salario_final:.2f} R$')
else:
    salario_final1 = (salario * 0.15) + salario
    print(f'O salário com aumento é o seguinte {salario_final1:.2f} R$')
