from random import randint
print('=-' * 15)
print(f'VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
jogador = vitorias = 0
computador = 0
parOuImpar = resp = ''
while True:
    jogador = int(input('Digite um valor: '))
    parOuImpar = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    computador = randint(0, 10)
    if parOuImpar == 'P':
        parOuImpar = 'PAR'
    elif parOuImpar == 'I':
        parOuImpar = 'ÍMPAR'
    print('-' * 30)
    if (jogador + computador) % 2 == 0:
        resp = 'PAR'
    else:
        resp = 'ÍMPAR'
    if parOuImpar == resp:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} \033[32mDEU {resp}\033[m')
        print('-' * 30)
        print('\033[32mVOCÊ GANHOU\033[m')
        print('Vamos jogar novamente...')
        vitorias += 1
    else:
        break
print(f'Você jogou {jogador} e o computador {computador}. Total de {jogador + computador} \033[31mDEU {resp}\033[m')
print('\033[31mVocê PERDEU\033[m')
print('=-' * 15)
print(f'GAME OVER! Você venceu {vitorias} vezes.')
