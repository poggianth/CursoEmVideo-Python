soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número inteiro: '))
    cont += 1
    if num % 2 == 0:
        soma += num
print(f'Você informou {cont} números. A soma de todos os valores PARES digitados foi: {soma}')
