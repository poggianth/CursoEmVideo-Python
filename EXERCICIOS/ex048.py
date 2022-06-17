impares = 0
cont = 0
for c in range(1, 500):
    if c % 2 == 1 and c % 3 == 0:
        impares += c
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é de {impares}')
