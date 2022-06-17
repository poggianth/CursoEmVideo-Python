salario = float(input('Salário do funcionário: R$'))
aumento = (salario * 10) / 100
sf = salario + aumento
print(f'Quem ganhava R${salario:.2f} passa a ganhar: R${sf:.2f}')
if salario <= 1200:
    aumento = (salario * 15) / 100
    sf = salario + aumento
    print(f'Quem ganhava R${salario:.2f} passa a ganhar: R${sf:.2f}')
