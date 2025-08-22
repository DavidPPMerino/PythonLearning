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


# def moeda(n):
#     return f"R${n:.2f}"


""" Resolução Curso em Video """
def aumentar(preço = 0, taxa = 0):
    res = preço + (preço * taxa / 100)
    return res


def diminuir(preço = 0, taxa = 0):
    res = preço - (preço * taxa / 100)
    return res


def dobro(preço = 0):
    res = preço * 2
    return res


def metade(preço = 0):
    res = preço / 2
    return res


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.',',')
