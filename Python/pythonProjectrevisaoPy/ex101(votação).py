def verifica(n):
    from datetime import date
    atual = date.today().year
    idade = atual - n
    if idade < 16:
        return f'com {idade} anos: Não precisa votar...'
    if idade >= 18 and idade <= 70:
        return f'com {idade} anos: Voto Obrigatório!'
    if idade > 70 or 16 >= idade <= 17:
        return f'com {idade} anos: Voto Opcional...'
    


#__main__{
print('¬' * 30)
nasc = int(input('Ano de nascimento: '))
print(verifica(nasc))
#}