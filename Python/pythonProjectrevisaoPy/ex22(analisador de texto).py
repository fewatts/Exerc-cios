from time import sleep
nome = str(input('Digite seu nome completo: ')).strip()
print('\033[7m Analisando seu nome... \033[m')
sleep(1)
separa = nome.split()
print(f'''Seu nome em maiúsculas é {nome.upper()}
Seu nome em minúsculas é {nome.lower()}
Ao total seu nome tem  letras {len(nome) - nome.count(' ')}
seu primeiro nome é {separa[0]} e tem {nome.find(' ')} letras.''')
