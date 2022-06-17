distancia = float(input('Qual é a distância da viagem? (Km)'))
print(f'Você está prestes a começar uma viagem de {distancia}Km.')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preço da viagem é de: R${preco:.2f}')
