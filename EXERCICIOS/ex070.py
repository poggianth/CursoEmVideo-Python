print('-' * 30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 30)
total = maisDe1000 = contador = produtoMaisBarato = 0
nomeMaisBarato = ''
while True:
    nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    total += preco
    contador += 1
    if contador == 1 or preco < produtoMaisBarato:
        nomeMaisBarato = nome
        produtoMaisBarato = preco
    if preco > 1000:
        maisDe1000 += 1
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]'.strip().upper()[0]))
    if continuar == 'N':
        break
print('')
print('-' * 10, 'FIM DO PROGRAMA', '-' * 10)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maisDe1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeMaisBarato} que custa R${produtoMaisBarato:.2f}')
