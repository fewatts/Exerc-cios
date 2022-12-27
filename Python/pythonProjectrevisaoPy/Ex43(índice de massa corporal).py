peso = float(input('Qual o seu peso em Kg? '))
altura = float(input('Qual a sua altura em metros? '))
imc = peso / (altura ** 2)
print(f'O seu IMC é de {imc:.1f} KG/M quadrado')
if imc < 18.5:
    print('Você está abaixo do peso, procure um nutricionista!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal, Parabéns!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso, procure um nutricionista!')
elif 30 <= imc < 40:
    print('Você está com obesidade, procure um nutricionista!')
else:
    print('Você está com obesidade mórbida, procure um nutricionista IMEDIATAMENTE!')
