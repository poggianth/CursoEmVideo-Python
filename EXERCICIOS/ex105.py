def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas ds alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)

    if sit:
        if r['Média'] >= 7:
            r['Situação'] = '\033[32mBOA\033[m'

        elif r['Média'] >= 5:
            r['Situação'] = '\033[33mRAZOÁVEL\033[m'

        else:
            r['Situação'] = '\033[31mRUIM\033[m'

    return r


# Programa principal
resp = notas(5.5, 2.5, 8.5, sit=True)
print(resp)
