def aumentar(num, a, f=False):
    r = num + (num * (a / 100))
    if f:
        return f'{r:.2f} R$'
    else:
        return r


def diminuir(num, d, f=False):
    r = num - (num * (d / 100))
    if f:
        return f'{r:.2f} R$'
    else:
        return r


def dobro(num, f=False):
    r = num * 2
    if f:
        return f'{r:.2f} R$'
    else:
        return r
    

def metade(num, f=False):
    r = num / 2
    if f:
        return f'{r:.2f} R$'
    else:
        return r


def resumo(n, a, r):
    msg = 'RESUMO VALOR'
    tam = len(msg) + 20
    print('¬' * tam)
    print(f'          {msg}')
    print('¬' * tam)
    print(f'''{"Preço analisado: ":<}{n:>} R$
{"Dobro do preço:":<} {dobro(n, f=True):>}
{"Metade do preço:":<} {metade(n, f=True):>}
{a}{"% de aumento:" :<} {aumentar(n, a, f=True):>}
{r}{"% de redução:" :<} {diminuir(n, a, f=True):>}''')
    print('¬' * tam)
