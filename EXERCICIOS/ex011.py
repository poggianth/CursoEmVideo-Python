altura = float(input('Altura: '))
largura = float(input('Largura: '))
area = (largura + largura) + (altura + altura)
print(f'A área dessa parede é de {area:.1f}')
tinta = area / (2*2)
print(f'E para pintar essa parede, você vai precisar de {tinta} litros de tinta.')
