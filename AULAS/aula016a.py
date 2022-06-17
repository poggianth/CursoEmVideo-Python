lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for c in lanche:
    print(f'Eu vou comer: {c}')

print('-' * 40)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('-' * 40)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('')
print('Essas foram as comidas presentes na tupla LANCHE')
