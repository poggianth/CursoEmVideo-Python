matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somaterceira = maiorsegundalinha = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor da posicão [{linha}, {coluna}]: '))

print('-=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()

print('-=' * 30)

print(f'A soma dos valores pares digitados é {somapar}')

for linha in range(0, 3):
    somaterceira += matriz[linha][2]

print(f'A soma dos valores da terceira coluna é {somaterceira}')

for c in range(0, 3):
    if c == 0:
        maiorsegundalinha = matriz[1][c]
    elif matriz[1][c] > maiorsegundalinha:
        maiorsegundalinha = matriz[1][c]

print(f'O maior valor da segunda linha é {maiorsegundalinha}')
