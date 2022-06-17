galera = list()
pessoa = dict()
mulheres = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite somente M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'NS':
            break
        print('ERRO! Por favor, digite somente S ou N')
    if continuar == 'N':
        break

print('-=' * 30)

print(f'A) Ao todo temos {len(galera)} cadastradas.')
media = soma / len(galera)

print(f'B) A média da idade do grupo é de {media:5.2f} anos.')

print(f'C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')

print()

print(f'D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

print('PROGRAMA ENCERRADO!!!')
