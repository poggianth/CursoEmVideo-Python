print('=' * 30)
primeirotermo = int(input('Digite o Primeiro termo da sua PA: '))
razao = int(input('Informe a razão da sua PA: '))
decimotermo = primeirotermo + 10 * razao
for c in range(primeirotermo, decimotermo, razao):
    print(c, end='→ ')
print('ACABOU')
