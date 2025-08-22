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


# def resumo(n, upperc, downperc):
#     print('-' * 40)
#     print('RESUMO DO VALOR'.center(40))
#     print('-' * 40)
#     print('Preço analisado:'.ljust(29), end='')
#     print(f'{moeda(n)}'.ljust(11))
#     print('Dobro do preço:'.ljust(29), end='')
#     print(f'{dobro(n, True)}'.ljust(11))
#     print('Metade do preço:'.ljust(29), end='')
#     print(f'{metade(n, True)}'.ljust(11))
#     print(f'{upperc}% de aumento:'.ljust(29), end='')
#     print(f'{aumentar(n, upperc, True)}'.ljust(11))
#     print(f'{downperc}% de redução:'.ljust(29), end='')
#     print(f'{diminuir(n, downperc, True)}'.ljust(11))
#     print('-' * 40)


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


def resumo(preço = 0, taxaa = 10, taxar = 5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'Com {taxar}% de aumento: \t{diminuir(preço, taxar, True)}')
    print('-' * 30)