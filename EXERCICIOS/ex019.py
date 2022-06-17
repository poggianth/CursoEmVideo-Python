import random
aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))
lista = [aluno4, aluno3, aluno2, aluno1]
sorteado = random.choice(lista)
print(f'O sorteado foi: {sorteado}')
