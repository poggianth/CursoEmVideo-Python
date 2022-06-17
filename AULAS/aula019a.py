pessoas = {'nome': 'Thiago', 'Sexo': 'M', 'Idade': 16}
# pessoas['nome'] = 'Gustavo' (O nome passa a ser Gustavo)
# del pessoas['Sexo'] (Apagou o Sexo)
pessoas['peso'] = 77.5 # adicionou o elemento PESO no dicionário
print()
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
for k in pessoas.keys():
    print(k)
print()
for k in pessoas.values():
    print(k)
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
