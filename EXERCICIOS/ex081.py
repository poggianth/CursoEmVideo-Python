valores = []
cont = 0
while True:
    valores.append(int(input('Digite um número: ')))
    cont += 1
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
valores.sort(reverse=True)
print('-=' * 30)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista e se encontra na posição {valores.index(5) + 1}')
else:
    print('O valor 5 não faz parte da lista!')
