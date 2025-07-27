""" Enunciado:
        Crie um programa que leia um número inteiro e mostre
        na tela se ele é PAR ou ÍMPAR.
"""

" V1.0 "
# n = int(input('Escreva um numero: '))
# print(f'A analisar o numero {n}')
# if n % 2 == 0:
#     print('O seu numero é Par!')
# else:
#     print('O seu numero é Impar!')

""" Resolução Curso em Video """
número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print(f'O número {número} é PAR')
else:
    print(f' O número {número} é ÍMPAR')