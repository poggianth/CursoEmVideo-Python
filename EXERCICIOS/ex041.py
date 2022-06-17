print('-' * 30)
print('DESCUBRA QUAL É A SUA CATEGORIA')
print('-' * 30)
idade = int(input('Digite a sua idade: '))
if idade <= 9:
    print('Você é da categoria MIRIM!')
elif idade <= 14:
    print('Você é da categoria INFANTIL!')
elif idade <= 19:
    print('Você é da categoria JUNIOR!')
elif idade <= 25:
    print('Você é da categoria SÊNIOR!')
elif idade > 25:
    print('Você é da cateoria MASTER!')
