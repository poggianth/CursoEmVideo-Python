teste = list()
teste.append('Thiago')
teste.append(16)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
