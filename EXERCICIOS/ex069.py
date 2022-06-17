idade = maioresDe18 = quantosHomens = mulheresMenos20 = 0
sexo = continuar = ''
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        maioresDe18 += 1
    if sexo == 'M':
        quantosHomens += 1
    if sexo == 'F' and idade < 20:
        mulheresMenos20 += 1
    print('-' * 30)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('')
print('=' * 6, 'FIM DO PROGRAMA', '=' * 6)
print(f'Total de pessoas maiores de 18 anos: {maioresDe18}')
print(f'Ao todo temos {quantosHomens} homens cadastrados')
print(f'E temos {mulheresMenos20} mulheres com menos de 20 anos.')
