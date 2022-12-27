from datetime import date
while True:
    sexo = str(input('Qual seu sexo?[m/f] '))
    if sexo in 'Ff':
        print('Sendo do sexo feminino, o alistamento obrigatório não se aplica!')
        break
    nascimento = int(input('Qual o ano do seu nascimento? '))
    atual = date.today().year
    anos = atual - nascimento
    alistamento = anos - 18
    alistamento_menor = 18 - anos
    if anos == 18:
        print('Você deve se alistar imediatamente!')
    if anos > 18:
        print(f'Quem nasceu em {nascimento} tem {anos} anos em {atual}\nVocê deveria ter se alistado há {alistamento} anos')
    if anos < 18:
        print(f'Ainda há tempo para respirar, seu alistamento é em {alistamento_menor} anos')
