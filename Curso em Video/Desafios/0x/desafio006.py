""" Enunciado:
        Crie um algoritmo que leia um número e mostre o seu dobro, triplo e
        raiz quadrada.
"""

" V1.0 "
# n = int(input('Escreva um numero: '))
# x2 = n*2
# x3 = n*3
# rq = n**(1/2)
# print('Escreveste o número {} !!!\n > o dobro é {}!!\n >> o triplo é {}!!!'.format(n, x2,x3), end='\n >>>><<<< \n')
# print('A raiz quadrada de {} é {:.3f}'.format(n, rq))

""" Resolução Curso em Video """
n = int(input('Digite um número: '))
print(f'O dobro de {n} vale {n*2}')
print(f'O triplo de {n} vale {n*3}, \nA raiz quadrada de {n} é igual a {pow(n, (1/2)):.2f}')