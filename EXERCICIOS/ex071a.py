print('=' * 30)
print('{:^30}'.format('BANCO DO TH'))
print('=' * 30)
saque = int(input('Qual valor você quer sacar? R$'))
total = saque
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO DO TH! Tenha um bom dia!')
