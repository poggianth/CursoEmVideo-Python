from random import randint
from time import sleep
print('-' * 10, 'JOGO DA ADIVINHAÇÃO', '-' * 10)
computador = randint(0, 5)
jogador = int(input('Qual foi o número pensado entre 0 e 5?: '))
print('PROCESSANDO...')
sleep(1.5)
if jogador == computador:
    print(f'O número pensado foi {computador}. VOCÊ VENCEU!!! :)')
else:
    print(f'O número pensado foi {computador}. VOCÊ PERDEU!!! :(')
