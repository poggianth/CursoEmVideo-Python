nome = str(input('Digite seu nome completo: ')).strip()
print(f'O seu nome completo em maiúsculo fica assim: {nome.upper()}')
print(f'O seu nome completo em minúscolo fica assim: {nome.lower()}')
print('O seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
primeiro = nome.split()
print(f'O seu primeiro nome possui', nome.find(' '), 'letras')