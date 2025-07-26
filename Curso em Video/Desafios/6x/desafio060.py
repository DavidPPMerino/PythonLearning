""" Enunciado:
        Faça um programa que leia um número qualquer e mostre o seu fatorial.
        Ex:
        5! = 5x4x3x2x1 = 120
"""

" V1.0 "
# n = int(input('Escreva um numero: '))
# totalx = 1
# print(f'{n}! =', end=' ')
# while n != 0:
#     if n == 1:
#         print(f'{n}=', end=' ')
#
#     elif n > 1:
#         print(f'{n}x', end='')
#     totalx *= n
#     n -= 1
# print(totalx)

""" Resolução com modulo Curso em Video """

# from math import factorial
# n = int(input('Digite um número para calcular seu Fatorial: '))
# f = factorial(n)
# print(f'O fatorial de {n} é {f}')

""" Resolução Curso em Video """
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

""" Desafiou fazer o programa usando o "for" """