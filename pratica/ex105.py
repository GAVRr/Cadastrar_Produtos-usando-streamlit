
def notas(*num , sit=False):
    '''
    -> Cálculo da media de notas de um aluno
    :param num: notas do aluno
    :param sit: mostrar situação do aluno
    :return: retornar as notas e a média
    '''
    boletim = dict()
    boletim['Total'] = len(num)
    boletim['Maior'] = max(num)
    boletim['Menor'] = min(num)
    boletim['Media'] = sum(num)/len(num)
    if sit:
        if boletim['Media'] >=7:
            boletim['Situação'] = 'BOA'
        elif boletim['Media'] >= 5:
            boletim['Situação'] = 'Razoavél'
        else:
            boletim['Situação'] = 'Ruim'

    return boletim






resp = notas(5,5,9,8 , sit=True)
print(resp)
help(notas)