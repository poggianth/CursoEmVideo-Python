from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('=-=' * 15)
print('VAMOS JOGAR JOKNEPÔ!')
print('=-=' * 15)
print('''OPÇÕES:
[0] = PEDRA
[1] = PAPEL
[2] = TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!')
sleep(0.5)
print('-=' * 15)
print(f'Computador jogou {itens[computador]} \nJogador jogou {itens[jogador]}')
print('-=' * 15)
if computador == 0: #COMPUTADOR JOGOU PEDRA
    if jogador == 1:
        print('\033[0;32mJogador Venceu!\033[m')
    elif jogador == 0:
        print('EMPATE!')
    elif jogador == 2:
        print('\033[0;31mComputador Venceu!\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 2:
        print('\033[0;32mJogador Venceu!\033[m')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 0:
        print('\033[0;31mComputador venceu!\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('\033[0;32mJogador Venceu!\033[m')
    elif jogador == 2:
        print('EMPATE!')
    elif jogador == 1:
        print('\033[0;31mComputador Venceu!\033[m')
    else:
        print('JOGADA INVÁLIDA')
