from time import sleep


def maior(*num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in range(0, len(num)):
        print(num[n], end=' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) == 0:
        print('O maior valor informado foi 0')
    else:
        print(f'O maior valor informado foi {max(num)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
