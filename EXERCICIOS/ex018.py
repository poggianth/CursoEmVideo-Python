from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de: {seno:.2f}')
coseno = cos(radians(angulo))
print(f'O ângulo de {angulo} tem o COSENO de: {coseno:.2f}')
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem a TANGENTE de: {tangente:.2f}')
