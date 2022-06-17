print('-=' * 15)
print('ESCOPO DE VÁRIAVEIS')
print('-=' * 15)


def funcao(n2):
    global n1
    n1 = 4
    n2 += 4
    n3 = 2
    print(f'n1 DENTRO vale {n1}')
    print(f'n2 DENTRO vale {n2}')
    print(f'n3 DENTRO vale {n3}')

# Programa principal


n1 = 5
funcao(n1)
print(f'n1 FORA vale {n1}')
