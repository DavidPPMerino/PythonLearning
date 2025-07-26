""" Enunciado:
        Crie um programa que leia o nome completo de uma pessoa e mostre:
        → O nome com todas as letras maiúsculas e minúsculas.
        → Quantas letras ao todo (sem considerar espaços).
        → Quantas letras tem o primeiro nome.
"""

" V1.0 "
# n = input('Qual é o seu nome completo: ')
# print(f'O seu nome é {n}.')
# print(f'Nome Completo em maiusculas: {n.upper()}')
# print(f'Nome Completo em minusculas: {n.lower()}')
# print(f'Quantas letras tem no total: {len(n.replace(" ", ""))}')
# dividido = n.split()
# print(f'O primeiro nome tem {len(dividido[0])} letras.')

""" Resolução Curso em Video """
nome = str(input('Digite seu nome completo: ')).strip()
print('Analizando seu nome... ')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
# print(f'Seu primeiro nome tem {nome.find(' ')} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')