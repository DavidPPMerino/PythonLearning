""" Enunciado:
Faça um programa que tenha uma 'função' chamada 'área()', que receba as dimensões
de um terreno retangular (largura e comprimento) e mostre a 'área do terreno'.
"""

" V1.0 "
def area(a, b):
    x = a * b
    print(f'A área de um terreno de {a:.1f}x{b:.1f} é de {x:.1f}m²')

def titulo(txt):
    print('-=' * 25 + '-')
    print(txt.center(51))
    print('-=' * 25 + '-')


#Programa

titulo('Controle de terrenos')
a = float(input('Largura (m): '))
b = float(input('Comprimento (m): '))
print('-=' * 25 + '-')
area(a, b)
