""" Enunciado:
        Faça um programa que leia o comprimento do cateto oposto e do
        cateto adjacente de um triângulo retângulo, calcule e mostre o
        comprimento da hipotenusa.
"""

" V1.0 "
# from math import hypot
# x = float(input('um lado: '))
# y = float(input('outro lado: '))
# print(f'a hipotenusa de um triangulo com um lado {x} e outro lado {y} é {hypot(x, y):.2f}')

""" Resolução sem importação Curso em Video """
# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# print(f'A hipotenusa vai medir {hi:.2f}')

""" Resolução com importação Curso em Video """
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')
