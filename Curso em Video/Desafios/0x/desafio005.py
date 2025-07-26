""" Enunciado:
        Faça um programa que leia um número Inteiro e mostre na tela o seu
        sucessor e o seu antecessor.
"""

" V1.0 "
# n = int(input('Escreva um numero: '))
# a = n-1
# s = n+1
# print('Escreveste {} \n o seu sucessor é {} e o seu antecessor é {}'.format(n, s, a))

""" Resolução Curso em Video """
n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))
