from random import randint
from time import sleep
print('-' * 10, 'JOGO DA ADIVINHAÇÃO', '-' * 10)
palpites = 1
computador = randint(0, 10)
jogador = int(input('Qual foi o número pensado entre 0 e 10?: '))
print('PROCESSANDO...')
sleep(0.5)
while jogador != computador:
    print('\033[31mVocê errou\033[m, dê doutro palpite.')
    jogador = int(input('Qual foi o número pensado entre 0 e 10?: '))
    palpites += 1
    print('PROCESSANDO...')
    sleep(0.5)
print(f'O número pensado foi {computador}. \033[32mVOCÊ VENCEU\033[m e precisou de {palpites} palpites para acertar!!! :)')
