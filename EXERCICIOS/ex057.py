sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Opção inválida. Digite seu sexo: ')).strip().upper()
print(f'Ok, sexo {sexo} registrado com sucesso!')
