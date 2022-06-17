def ficha(nome=str(''), gols=0):
    if nome == '':
        nome = str('<desconhecido>')
    if gols == '':
        gols = 0
    print(f'O jogador {nome.capitalize()} marcou {gols} gol(s) no campeonato.')


# Programa principal

print('-' * 30)
jogador = str(input('Nome do jogador: '))
nGols = input('Números de gols: ')

if nGols.isnumeric():
    nGols = int(nGols)
else:
    nGols = 0

ficha(jogador, nGols)
