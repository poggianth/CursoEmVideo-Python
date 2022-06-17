soma = cont = maior = menor = 0
continuar = ''
while not continuar == 'N':
    num = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print(f'A média entre todos os valores digitados foi de {soma / cont:.1f}')
print(f'O maior número digitado foi: {maior}')
print(f'O menor número digitado foi: {menor}')
