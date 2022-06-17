print('=' * 30)
print('BANCO DO TH')
print('=' * 30)
casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
tempo = int(input('Em quantos anos você pretende pagar esta casa? '))
prestacao = casa / (tempo * 12)
print(f'Para pagar uma casa de R${casa:.2f} em {tempo} anos', end='')
print(f' a prestação mensal será de R${prestacao:.2f}')
if prestacao < salario * 30 / 100:
    print(f'\033[0;32mO empréstimo pode ser realizado!\033[m')
else:
    print('\033[0;31mO empréstimo não pode ser realizado pois o valor da prestação excedeu 30% do seu salário!\033[m')
