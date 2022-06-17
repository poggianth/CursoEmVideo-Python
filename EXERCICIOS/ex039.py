import datetime
nasc = int(input('Ano de nascimento:'))
atual = datetime.date.today().year
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade < 18:
    print(f'Não está na hora de se alistar, ainda falta {18 - idade} anos para o alistamento.')
    print(f'Seu alistamento será em {atual + (18 - idade)}')
elif idade == 18:
    print('Está na hora de se alistar IMEDIATAMENTE!')
elif idade > 18:
    print(f'Você já deveria ter se alistado  há {idade - 18} anos.')
    print(f'Seu alistamento foi em {atual - (idade - 18)}')
