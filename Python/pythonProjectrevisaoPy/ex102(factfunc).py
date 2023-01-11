def factorial(n, show=False):
    f = n
    for c in range(n, 0, -1):
        print(c, end=' ')
        r = f * n
        f -= 1
    return r


#__Main__{
factorial(7)
# }