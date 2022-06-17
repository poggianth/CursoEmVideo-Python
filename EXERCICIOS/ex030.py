num = int(input('Digite um número para saber se ele é par ou ímpar: '))
resultado = num % 2
if resultado == 0:
    print(f'O número {num} é PAR!')
else:
    print(f'O número {num} é ÍMPAR!')
