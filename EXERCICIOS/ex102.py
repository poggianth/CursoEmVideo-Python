def fatorial(n=1, show=False):
    """
    → Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor da Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c} x', end=' ')
            if c == 1:
                print('1 =', end=' ')
    print(f)


# Programa principal
numero = int(input('Quer calcular o fatorial de qual número?: '))
conta = str(input('Deseja mostrar a conta? [S/N]: ')).strip().upper()[0]
while conta not in 'SN':
    conta = str(input('Resposta inválida, digite somente [S/N]: ')).strip().upper()[0]
if conta == 'N':
    conta = False
if conta == 'S':
    conta = True
fatorial(numero, show=conta)
