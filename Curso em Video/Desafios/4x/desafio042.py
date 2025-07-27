""" Enunciado:
        Refaça o desafio 035 dos triângulos, acrescentando o recurso de
        mostrar que tipo de triângulo será formado:
        - Equilátero: todos os lados iguais
        - Isósceles: dois lados iguais
        - Escaleno: todos os lados diferentes
"""

" V1.0 "
# from time import sleep as slp
#
# print('\033[1;31m-'*10,'\033[4;33mCalculadora de Triangulos\033[m','\033[1;31m-\033[m'*10)
#
# r1 = float(input('\033[0;33mEscreva o tamanho da primeira reta: '))
# print('\033[1;31m-'*42)
# r2 = float(input('\033[0;33mEscreva o tamanho da segunda reta: '))
# print('\033[1;31m-'*42)
# r3 = float(input('\033[0;33mEscreva o tamanho da terceira reta: '))
# print('\033[1;31m-'*42)
#
# print(f'A analisar as retas...'.center(42),'\033[m')
# slp(1)
#
# if not r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
#     print('Infelizmente não é possivel criar um triangulo!')
# else:
#     #if r1 == r2 and r1 == r3:
#     if r1 == r2 == r3:
#         print('Sim é possivel criar um triangulo Equilátero!')
#     #elif r1 != r2 and r1 != r3 and r2 != r3:
#     elif r1 != r2 != r3 != r1:
#         print('Sim é possivel criar um triangulo Escaleno!')
#     else:
#         print('Sim é possivel criar um triangulo Isósceles')
#
""" Resolução Curso em Video """
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end= '')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
