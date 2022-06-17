print('-' * 30)
print('Descubra se você está no peso ideial!')
print('-' * 30)
peso = float(input('Digite o seu peso atual: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do PESO IDEAL!')
elif imc <= 25:
    print('Parabéns, você está no PESO IDEAL!')
elif imc <= 30:
    print('Cuidado, Você está ACIMA do Peso Ideal!')
elif imc <= 40:
    print('MUITA ATENÇÃO, você está com OBESIDADE! Se cuide!!')
elif imc > 40:
    print('Você está com OBESIDADE MÓRBIDA! PROCURE UM MÉDICO!!')
