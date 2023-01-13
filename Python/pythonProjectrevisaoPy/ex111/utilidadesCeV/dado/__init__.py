def leiadinheiro(msg):
    valido = False
    while not valido:
        dado = str(input(msg)).replace(',', '.').strip()
        if dado.isalpha() or dado == '':
            print(f'...404... {msg} não é válido')
        else:
            valido = True
            return float(msg)