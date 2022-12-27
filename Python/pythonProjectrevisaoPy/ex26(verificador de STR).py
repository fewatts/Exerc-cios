frase = str(input('Escreva uma frase: ')).upper().strip()
print(f'''A letra "a" aparece {frase.count("A")} vezes
A sua primeira posição é {frase.find("A")}
e sua última posição é {frase.rfind("A")}''')
