""" Funções parte 2 """

# Interactive Help
# docstrings
# Argumentos opcionais
# Escopo de variáveis
# Retorno de resultados

""" Interactive help """

# help() # Chama a função help na consola para sair escrever 'quit'
# help(print) # chama a função help relativa á função print

# print(input.__doc__) # outra forma de interactive help que pode nao ser igual

""" Docstring """

# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela.
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i 
#     while c <= f:
#         print(f'{c}', end='..')
#         c += p
#     print('FIM!')

# help(contador)

""" Argumentos opcionais """

# def somar(a=0, b=0, c=0): # c=0 transforma c num parametro opcional
#     """
#     -> Faz a soma de três valores e mostra o resultado na tela.
#     :param a: o primeiro valor
#     :param b: o segundo valor
#     :param c: o terceiro valor
#     Função criada por Gustavo Guanabara do canal CursoemVideo
#     """
#     s = a + b + c
#     print(f'A soma vale {s}')

# somar(3)

""" Escopo de variaveis """

# Escopo é o local onde a variavel vai ou nao existir

"Hipotese 1 Escopo global"
# def teste():
#     print(f'Na função teste, n vale {n}')
# # Programa Principal
# n = 2                           # variavel n funciona em todo o programa
# print(f'No programa principal, n vale {n}')
# teste()

"Hipotese 2 Escopo local"
# def teste():
#     x = 8
#     print(f'Na função teste, n vale {n}')
#     print(f'Na função teste, x vale {x}')
# # Programa Principal
# n = 2
# print(f'No programa principal, n vale {n}')
# teste()
# print(f'No programa principal, x vale {x}') # a variavel x so funciona na função contador

"Hipotese 3 Mesma variavel em ambos os escopos"
# def teste(b):
#     a = 8   # variavel local só funciona dentro da função
#     b += 4
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')

# a = 5       # variavel global funciona em todo o lugar desde que nao haja uma local
# teste(a)
# print(f'A fora vale {a}')

"Hipotese 4 Substituir variavel em ambos os escopos"
# def teste(b):
#     global a    # passa a usar a variavel global em vez da local
#     a = 8   
#     b += 4
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')

# a = 5       # variavel global funciona em todo o lugar desde que nao haja uma local
# teste(a)
# print(f'A fora vale {a}')

""" Retorno de valores """

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')
print(f'Dando um total de {somar(r1, r2, r3)}')