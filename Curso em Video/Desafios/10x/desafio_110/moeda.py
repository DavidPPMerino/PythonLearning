"""
Crie um módulo chamado 'moeda.py' que tenha as funções incorporadas 
'aumentar(n, perc)', 'diminuir(n, perc)', 'dobro(n)' e 'metade(n)'.
"""

" V1.0 "
def aumentar(n, perc, brl=False):
    x = n + (n * perc / 100)
    if brl:
        return f"R${x:.2f}"
    else:
        return x




def diminuir(n, perc, brl=False):
    x = n - (n * perc / 100)
    if brl:
        return f"R${x:.2f}"
    else:
        return x


def dobro(n, brl=False):
    x = n * 2
    if brl:
        return f"R${x:.2f}"
    else:
        return x


def metade(n, brl=False):
    x = n / 2
    if brl:
        return f"R${x:.2f}"
    else:
        return x


def moeda(n):
    return f"R${n:.2f}"


def resumo(n, upperc, downperc):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print('Preço analisado:'.ljust(16), end='')
    print(f'{moeda(n)}'.rjust(24))
    print('Dobro do preço:'.ljust(16), end='')
    print(f'{dobro(n, True)}'.rjust(24))
    print('Metade do preço:'.ljust(16), end='')
    print(f'{metade(n, True)}'.rjust(24))
    print(f'{upperc}% de aumento:'.ljust(16), end='')
    print(f'{aumentar(n, upperc, True)}'.rjust(24))
    print(f'{downperc}% de redução:'.ljust(16), end='')
    print(f'{diminuir(n, downperc, True)}'.rjust(24))
    print('-' * 40)

""" Resolução Curso em Video """
