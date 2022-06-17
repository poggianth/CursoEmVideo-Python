print()
print('Controle de Terrenos')
print('-' * 30)


def area(largura, comprimento):
    print(f'A área de um terrno {largura}x{comprimento} é de {largura*comprimento}m².')


area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
