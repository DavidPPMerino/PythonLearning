"""
Crie um módulo chamado 'moeda.py' que tenha as funções incorporadas 
'aumentar(n, perc)', 'diminuir(n, perc)', 'dobro(n)' e 'metade(n)'.
"""

" V1.0 "
# def aumentar(n, perc):
#     return n + (n * perc / 100) 


# def diminuir(n, perc):
#     return n - (n * perc / 100) 


# def dobro(n):
#     return n * 2


# def metade(n):
#     return n / 2


""" Resolução Curso em Video """
def aumentar(preço, taxa):
    res = preço + (preço * taxa / 100)
    return res


def diminuir(preço, taxa):
    res = preço - (preço * taxa / 100)
    return res


def dobro(preço):
    res = preço * 2
    return res


def metade(preço):
    res = preço / 2
    return res
