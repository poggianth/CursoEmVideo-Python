peso = float(input('Digite o peso da 1ª pessoa: '))
maior = peso
menor = peso
for pessoa in range(2, 6):
    peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))
    if peso >= maior:
        maior = peso
    if peso <= menor:
        menor = peso
print('-' * 30)
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
