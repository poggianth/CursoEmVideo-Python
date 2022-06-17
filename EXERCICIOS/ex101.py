from datetime import date


def voto(anodenascimento):
    """
    → Mostra se o voto é OBRIGATÓRIO, se a pessoa NÃO VOTA ou se o VOTO É OPCIONAL.
    :param anodenascimento: lê o ano de nascimento da pessoa e calcula a idade dela.
    :return: sem retorno
    Função crida por Thiago Melo
    """
    idade = atual - nascimento
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA')
    elif 16 <= idade < 18 or idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')


# Programa principal
print('-' * 30)
atual = date.today().year
nascimento = int(input('Em que ano você nasceu? '))
voto(nascimento)
