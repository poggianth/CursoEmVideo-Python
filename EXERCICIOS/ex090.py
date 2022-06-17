aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situação'] = '\033[32mAprovado!\033[m'

elif 5 <= aluno['media'] <= 6.5:
    aluno['situação'] = '\033[33mRecuperação!\033[m'

else:
    aluno['situação'] = '\033[31mReprovado!\033[m'

print('-=' * 30)
for k, v in aluno.items():
    print(f'    - {k.title()} é igual a {v}')
