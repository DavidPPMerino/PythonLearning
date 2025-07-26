"""Enunciado:
        Desenvolva um programa que leia as duas notas de um aluno,
        calcule e mostre a sua média.
"""

" v1.0 "
# print('===== Calculadora de medias =====')
# n1 = float(input('Escreva a sua primeira nota: '))
# n2 = float(input('Escreva a sua segunda nota: '))
# m = (n1+n2)/2
# print('As suas notas foram {:.1f} e {:.1f} \n A media das suas notas é {:.1f}'.format(n1, n2, m))

""" Resolução Curso em Video """
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
média = (n1 + n2) / 2
print(f'A média entre {n1} e {n2} é igual a {média:.1f}')