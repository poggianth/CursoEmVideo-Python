from math import factorial
vezes = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        vezes += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='')
print(f'\n\033[mO número {num}, foi divisivel {vezes} vezes.')
if vezes == 2:
    print('E por isso ele É PRIMO')
else:
    print(f'E por isso ele NÃO É PRIMO')
