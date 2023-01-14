def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO na criação do arquivo')
    else:
        print(f'{nome} criado!')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO...')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<40}{dado[1]:>3} Anos')
    finally:
        a.close()
        

def editararquivo(arq, nome='<Desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO...')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO...')
    finally:
        print(f'Registro de {nome} adicionado/a!')
        a.close()
    