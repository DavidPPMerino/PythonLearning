""" Enunciado:
        Faça um programa que leia um ângulo qualquer e mostre na tela o valor
        do seno, cosseno e tangente desse ângulo.
"""

" V1.0 "
# import math
# b = float(input('Escreva um angulo: '))
# a = math.radians(b)
# print(f'Sobre o angulo {b} o seno é {math.sin(a):.2f}, o coseno é {math.cos(a):.2f} e a tangente é {math.tan(a):.2f}')

""" Resolução Curso em Video """
from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ângulo))
print(f'O ângulo de {ângulo} tem o SENO de {seno:.2f}')
cosseno = cos(radians(ângulo))
print(f'O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(ângulo))
print(f'O ângulo de {ângulo} tem a TANGENTE de {tangente:.2f}')