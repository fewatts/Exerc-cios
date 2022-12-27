pilha = []
expre = str(input('Digite alguma expressão: '))
for l in expre:
    if l == '(':
        pilha.append('(')
    elif l == ')':
        if len(pilha) > 0:
            pilha.pop()
if len(pilha) == 0:
    print('Sua expressão é válida!!')
else:
    print('Sua expressão não é válida...')
