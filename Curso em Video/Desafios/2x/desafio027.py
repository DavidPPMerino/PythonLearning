""" Enunciado:
        Faça um programa que leia o nome completo de uma pessoa, mostrando
        em seguida o primeiro e o último nome separadamente.
"""

" V1.0 "
# nome = input('Escreva o seu nome completo: ').strip()
# n = nome.split()
# print(f'O seu primeiro nome é {n[0]} e o seu ultimo nome é {n[-1]}')

""" Resolução Curso em Video """
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')