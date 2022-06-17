preco = float(input('Preço do produto: R$'))
desconto = preco + (preco * 5 / 100)
print(f'O produto custava R${preco}, mas com 5% de desconto, ele irá sair por: R${desconto:.2f}')
