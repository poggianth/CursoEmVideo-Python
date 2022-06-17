print('-' * 30)
print('LOJINHA DO TH')
print('-' * 30)
valor = float(input('Digite o valor do produto: R$'))
print('''FORMAS DE PAGAMENTO:
      [0] à vista / cheque
      [1] à vista no cartão
      [2] em até 2x no cartão
      [3] 3x ou mais no cartão''')
pagamento = int(input('Qual é a forma de pagamento? '))
if pagamento == 0:
    print(f'Pagando à vista você ganha 10% de desconto! O valor final será de R${valor - (valor * 10)  / 100}')
elif pagamento == 1:
    print(f'Pagando à vista no cartão você ganha 5% de desconto! O valor final será de R${valor - (valor * 5) / 100}')
elif pagamento == 2:
    print(f'O valor final será de R${valor}')
elif pagamento == 3:
    print(f'Pagando em 3x ou mais no cartão acrescentará 20% de juros! O valor final será de R${valor + (valor * 20) / 100}')
