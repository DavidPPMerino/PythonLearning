""" Enunciado:
        Faça um programa que leia um numero Inteiro qualquer e mostre
        na tela a sua tabuada.
"""

" V1.0 "
# print('===== Tabuada de um numero =====')
# n = int(input('Escreva um numero: '))
# x1 = n*1
# x2 = n*2
# x3 = n*3
# x4 = n*4
# x5 = n*5
# x6 = n*6
# x7 = n*7
# x8 = n*8
# x9 = n*9
# x10 = n*10
# print('-' * 12)
# print(' ------------- \n Tabuada de {0} \n ------------- \n {0} x 1 = {1:2} \n {0} x  2 = {2} \n {0} x  3 = {3} \n {0} x  4 = {4} \n {0} x  5 = {5} \n {0} x  6 = {6} \n {0} x  7 = {7} \n {0} x  8 = {8} \n {0} x  9 = {9} \n {0} x 10 = {10} \n -------------'.format(n, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10))

""" Resolução Curso em Video """
num = int(input('Digite um numero para ver sua tabuada: '))
print('-' * 12)
print(f'{num} x {1:2} = {num*1}')
print(f'{num} x {2:2} = {num*2}')
print(f'{num} x {3:2} = {num*3}')
print(f'{num} x {4:2} = {num*4}')
print(f'{num} x {5:2} = {num*5}')
print(f'{num} x {6:2} = {num*6}')
print(f'{num} x {7:2} = {num*7}')
print(f'{num} x {8:2} = {num*8}')
print(f'{num} x {9:2} = {num*9}')
print(f'{num} x {10:2} = {num*10}')
print('-' * 12)
