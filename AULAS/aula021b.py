print('-=' * 15)
print('PARÂMETROS OPCIONAIS')
print('-=' * 15)


def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o treceiro valor
    Função criada por Thiago Melo.
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(c=2, a=3, b=5)
somar(3, 2, 5)
somar(8, 4)
somar()

