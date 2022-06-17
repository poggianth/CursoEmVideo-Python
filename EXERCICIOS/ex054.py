import datetime
atual = datetime.date.today().year
menores = 0
maiores = 0
for c in range(1, 8):
    nasc = int(input(f'Ano de nascimento da {c}ª pessoa:'))
    if atual - nasc < 21:
        menores += 1
    else:
        maiores += 1
print('-' * 30)
print(f'{menores} pessoas ainda NÃO atingiram a maioridade.')
print(f'E {maiores} pessoas já são maiores.')
