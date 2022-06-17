valores = []
while True:
    num = (int(input('Digite um valor: ')))
    if num not in valores:
        valores.append(num)
        print('\033[32mValor adicionado com sucesso...\033[m')
    else:
        print('\033[31mValor duplicado! Não vou adicionar...\033[m')

    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print('-=' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')
