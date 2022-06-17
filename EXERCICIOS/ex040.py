n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'A sua média foi {media}! Você está \033[0;31mREPROVADO\033[m')
elif media > 7:
    print(f'A sua média foi {media}! Você está \033[0;32mAPROVADO\033[m')
else:
    print(f'A sua média foi {media}! Você está de \033[0;33mRECUPERAÇÃO\033[m')
