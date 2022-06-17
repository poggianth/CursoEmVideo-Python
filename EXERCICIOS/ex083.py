expressao = str(input('Digite a expressão: '))
cont = 0
for simbolo in expressao:
    if simbolo == '(':
        cont += 1
    if simbolo == ')':
        cont -= 1
if cont == 0:
    print('A expressão é válida!')
else:
    print('A expressão não é válida!')
