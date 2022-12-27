pilha = []
frase = str(input('Digite alguma expressão: '))
for i in frase:
    if i == '(':
        pilha.append(i)
    elif i == ')':
        if len(pilha) > 0:
            pilha.pop()
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida...')
