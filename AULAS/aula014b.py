n = 1
par = impar = 0
while n != 999:
    n = int(input('Digite um valor [999 para sair]: '))
    if n != 999:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')