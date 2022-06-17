primeirotermo = int(input('Digite o primeiro termo a sua PA: '))
razao = int(input('Informe a razão desta PA: '))
cont = 10
while cont > 0:
    print(f'{primeirotermo} → ', end='')
    primeirotermo += razao
    cont -= 1
    if cont == 0:
        print('PAUSA')
        cont = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
