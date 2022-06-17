salario = float(input('Digite o salário do funcionário: R$'))
ns = salario + (salario * 15 / 100)
print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, irá receber R${ns:.2f}')
