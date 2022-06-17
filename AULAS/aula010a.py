tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('---FIM---')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'A sua média foi: {media:.1f}')
if media >= 6:
    print('A sua média foi boa! PARABÉNS!')
else:
    print('A sua média foi ruim! ESTUDE MAIS!')
