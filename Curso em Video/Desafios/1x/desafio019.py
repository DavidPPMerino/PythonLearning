""" Enunciado:
        Um professor quer sortear um dos seus quatro alunos para apagar
        o quadro. Faça um programa que ajude ele, lendo o nome deles e
        escrevendo o nome do escolhido.
"""

" V1.0 "
# import random
# nomes = input('Escreva os nomes separados por virgula: ')
# esc = nomes.split(', ')
# print(f'O vencedor foi {random.choice(esc)}')

""" Resolução Curso em Video """
from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')