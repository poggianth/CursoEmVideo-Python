from math import factorial
num = int(input('Digite um número para saber o seu factorial: '))
fac = num
print(f'Calculando {num}! = ', end='')
while fac > 0:
    print(fac, end='')
    print(' x ' if fac > 1 else ' = ', end='')
    fac -= 1
print(factorial(num))
