primeirotermo = int(input('Digite o primeiro termo a sua PA: '))
razao = int(input('Informe a razão desta PA: '))
termo = primeirotermo
cont = 1
total = 0
mostrarmais = 10
while mostrarmais != 0:
    total = total + mostrarmais
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mostrarmais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
