nome = str(input('Digite seu nome: ')).strip().split()
primeiro = nome[0]
ultimo = len(nome)
print(f'Primeiro nome: {primeiro}')
print(f'Último nome: {nome[ultimo - 1]}')
