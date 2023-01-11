def factorial(n, show=False):
    """
    ->Calcula o fatorial do input
    :param n: O número para obter fatorial
    :param show: Falso não mostra o cálculo e true mostra
    :return: retorna o valor final do cálculo
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#__Main__{
print(factorial(9, show=True))
# }