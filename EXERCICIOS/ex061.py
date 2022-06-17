primeirotermo = int(input('Digite o primeiro termo a sua PA: '))
razao = int(input('Informe a razão desta PA: '))
termo = primeirotermo
cont = 1
while cont <= 10:
    print(f'{termo} → ', end='')
    termo += razao
    cont += 1
print('FIM')
