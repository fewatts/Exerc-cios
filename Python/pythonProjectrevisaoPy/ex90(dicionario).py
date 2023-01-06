aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print('¬' * 40)
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] == 6:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for i, v in aluno.items():
    print(f'>>>> {i} é igual a {v}')
