idades = 0
idademaisvelho = 0
nomehomemmaisvelho = ''
mulheresmenos20 = 0
for p in range(1, 5):
    print('-' * 5, f'{p}ª pessoa', '-' * 5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M / F]: ')).strip().upper()
    idades += idade
    if p == 1 and sexo == 'Mm':
        idademaisvelho = idade
        nomehomemmaisvelho = nome
    if sexo == 'M'and idade > idademaisvelho:
        idademaisvelho = idade
        nomehomemmaisvelho = nome
    if sexo == 'F' and idade < 20:
        mulheresmenos20 += 1
media = idades / 4
print('=' * 30)
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {idademaisvelho} e se chama {nomehomemmaisvelho.capitalize()}.')
print(f'Ao todo são {mulheresmenos20} com menos de 20 anos.')
