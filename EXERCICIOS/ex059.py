opcao = ''
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outo valor: '))
while not opcao == 5:
    print('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] ver o maior valor digitado
[ 4 ] digitar novos números
[ 5 ] sair do programa
''')
    opcao = int(input('Qual é a sua opção: '))
    if opcao == 1:
        print(f'A soma entre {v1} + {v2} = {v1 + v2}')
    if opcao == 2:
        print(f'A multiplicação entre {v1} * {v2} = {v1 * v2}')
    if opcao == 3:
        if v1 > v2:
            print(f'O maior valor digitado foi {v1}')
        elif v2 > v1:
            print(f'O maior valor digitado foi {v2}')
        elif v1 == v2:
            print('Não existe valor maior, os dois valores são iguais.')
    if opcao == 4:
        v1 = int(input('Digite um novo valor: '))
        v2 = int(input('Digite outo novo valor: '))
print('Obrigado por utilizar este programa!!!')
