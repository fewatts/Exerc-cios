num = int(input('Informe um número: '))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 100 % 10
print(f'''O número informado corresponde a: 
{uni} unidades
{dez} dezenas
{cen} centenas e
{mil} milhares...''')
