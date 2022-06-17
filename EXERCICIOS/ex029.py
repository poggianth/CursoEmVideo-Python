velocidade = float(input('Digite a velocidade do carro: '))
valor = (velocidade - 80) * 7
if velocidade <= 80.0:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Você foi multado por exceder o limite de velocidade (80Km/h)')
    print(f'O valor a ser pago é de: R${valor:.2f}')
