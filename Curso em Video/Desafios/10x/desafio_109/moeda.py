"""
Crie um módulo chamado 'moeda.py' que tenha as funções incorporadas 
'aumentar(n, perc)', 'diminuir(n, perc)', 'dobro(n)' e 'metade(n)'.
"""

" V1.0 "
# def aumentar(n, perc, brl=False):
#     x = n + (n * perc / 100)
#     if brl:
#         return f"R${x:.2f}"
#     else:
#         return x




# def diminuir(n, perc, brl=False):
#     x = n - (n * perc / 100)
#     if brl:
#         return f"R${x:.2f}"
#     else:
#         return x


# def dobro(n, brl=False):
#     x = n * 2
#     if brl:
#         return f"R${x:.2f}"
#     else:
#         return x


# def metade(n, brl=False):
#     x = n / 2
#     if brl:
#         return f"R${x:.2f}"
#     else:
#         return x


# def moeda(n):
#     return f"R${n:.2f}"



""" Resolução Curso em Video """
def aumentar(preço = 0, taxa = 0, formato = False):
    res = preço + (preço * taxa / 100)
    return res if format is False else moeda(res)


def diminuir(preço, taxa = 0, formato = False):
    res = preço - (preço * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preço = 0, formato = False):   
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço = 0, formato = False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.',',')
