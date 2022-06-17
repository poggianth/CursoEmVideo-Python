print('-=-' * 15)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 15)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As medidas acima podem formar um triângulo!!')
else:
    print('As medidas acima NÃO podem formar um triângulo!!')
