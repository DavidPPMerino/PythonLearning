""" Enunciado:
        O mesmo professor do desafio anterior quer sortear a ordem de
        apresentação de trabalhos dos alunos. Faça um programa que
        leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

" V1.0 "
# import random
# nomes = input('Escreva o nome dos alunos separado por virgula: ')
# ln = nomes.split(', ')
# brl = random.shuffle(ln)
# print(f'Os nomes introdozidos foram {nomes}')
# print('Aqui está a lista baralhada')
# print(ln)

""" Resolução Curso em Video """
from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação será ')
print(lista)