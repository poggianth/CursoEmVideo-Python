galera = list()
dado = list()
totmaior = totmenor = 0

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #A LISTA GALERA VAI RECEBER UMA CÓPIA DE DADO
    dado.clear() #QUE LOGO DEPOIS SERÁ LIMPADO, ATÉ ACABAR O LAÇO

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1

print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')
