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



""" Resolução Curso em Video """
