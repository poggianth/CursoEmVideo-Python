print('=' * 30)
print('{:^30}'.format('BANCO DO TH'))
print('=' * 30)
saque = int(input('Qual valor você quer sacar? R$'))
notas50 = saque // 50
notas20 = (saque - (notas50 * 50)) // 20
notas10 = (saque - (notas50 * 50) - (notas20 * 20)) // 10
notas1 = (saque - (notas50 * 50) - (notas20 * 20) - (notas10 * 10)) // 1
if notas50 > 0:
    print(f'Total de {notas50} cédulas de R$50')
if notas20 > 0:
    print(f'Total de {notas20} cédulas de R$20')
if notas10 > 0:
    print(f'Total de {notas10} cédulas de R$10')
if notas1 > 0:
    print(f'Total de {notas1} cédulas de R$1')
print('=' * 30)
print('Volte sempre ao BANCO DO TH! Tenha um bom dia!')
