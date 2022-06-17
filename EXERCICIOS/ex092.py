import datetime
atual = datetime.date.today().year

dados = dict()
dados['nome'] = str(input('Nome: '))
dados['idade'] = (atual - int(input('Ano de nascimento: ')))
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de cotratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - atual

print('-=' * 30)

for k, v in dados.items():
    print(f'    - {k.title()} tem o valor {v}')
