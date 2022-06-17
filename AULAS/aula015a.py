n = soma = 0
while True:
    n = int(input('Digite um número [999 para sair]: '))
    if n == 999:
        break
    soma += n
print(f'A soma dos números digitados foi {soma}')
