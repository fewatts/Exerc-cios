def notas(* números, sit=False):
    aluno = {}
    print('¬' * 50)
    aluno['total'] = len(números)
    aluno['maior'] = max(números)
    aluno['menor'] = min(números)
    aluno['média'] = sum(números
    ) / len(números)
    if sit:
        if aluno['média'] <= 6:
            aluno['situação'] = 'RUIM'
        else:
            aluno['situação'] = 'BOA!'    
    return aluno


#__Main__{
resp = notas(5.5, 1.5, 2.5, 7, 1, sit=True)
print(resp)
# }