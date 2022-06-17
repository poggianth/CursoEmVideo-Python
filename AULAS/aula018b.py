galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][0])
print(galera[2][1])
print(galera[len(galera) - 1])
print()
print('Geral')
for p in galera:
    print(p)
print()
print('Somente os nomes: ')
for p in galera:
    print(p[0])
print()
print('Somente as idades: ')
for p in galera:
    print(p[1])
print()
print('Nome e idade:')
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
