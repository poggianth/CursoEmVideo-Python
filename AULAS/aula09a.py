frase = 'Curso em Vídeo Python'

print('')

print('-' * 10, 'FATIAMENTO', '-' * 10)
print('Do começo até o final pulando de 2 em 2 ==', frase[::2])
print('Do 9° até o 13° == ', frase[9:14])
print('Do 9° até o 21° pulando de 2 em 2 == ', frase[9:21:2])
print('Do começo até o 13°', frase[:14])

print('')

print('-' * 10, 'ANÁLISE', '-' * 10)
print('Quantidade de caracteres na frase == ', len(frase))
print('Conta quantas letras o tem na frase == ', frase.count('o'))
print('Conta quantas letras o tem na frase desde o começo até a 12° letra == ', frase.count('o', 0, 13))
print('Procura aonde começa a letra / frase (deo) == ', frase.find('deo'))
print('Mandou procurar (Android), não achou == ', frase.find('Android'))
print('Verifica se existe a letra / frase na frase == ', 'Curso' in frase)

print('')

print('-' * 10, 'TRANSFORMAÇÃO', '-' * 10)
print('Substitui a palavra escolhida pela palavra escolhida == ', frase.replace('Python', 'Android'))
print('Deixa a frase toda em maiúsculo == ', frase.upper())
print('Deixa a frase em minúsculo == ', frase.lower())
print('Deixa somente o primeiro letra da frase em maiúsculo == ', frase.capitalize())
print('Cada letra depois de um espaço, fica em maiúsculo == ', frase.title())
frase = '   Aprenda Python  '
print(frase)
print('Remove todos os espaços inúteis == ', frase.strip())
print('Remove todos os espaços inúteis da direita == ', frase.rstrip())
print('Remove todos os epaços inúteis da esquerda == ', frase.lstrip())

print('')

print('-' * 10, 'DIVISÃO', '-' * 10)
print('Faz uma divisão onde tiver espaço. (cria uma lista de todas as palavras da frase == )', frase.split())

print('')

print('-' * 10, 'JUNÇÃO', '-' * 10)
print('Junta os elementos de frase usando um separador  (-) == ', '-'.join(frase))
