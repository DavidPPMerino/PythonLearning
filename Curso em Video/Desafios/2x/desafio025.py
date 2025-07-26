""" Enunciado:
        Crie um programa que leia o nome de uma pessoa e diga se ela tem
        ?SILVA' no nome.
"""

" V1.0 "
# nome = input('Escreva o seu nome completo: ').strip()
# print(f'Você tem "Silva" no nome: {'silva' in nome.lower().split()}')

""" Resolução Curso em Video """
nome = str(input('Qual é seu nome completo? ')).strip()
print(f'Seu nome tem Silva? {'silva' in nome.lower()}')