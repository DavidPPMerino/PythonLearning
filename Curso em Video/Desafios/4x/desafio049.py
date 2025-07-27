""" Enunciado:
        Refaça o desafio 009, mostrando a 'tabuada' de um número que o usuário
        escolher, só que agora utilizando um 'laço for'.
"""

" V1.0 "
# print('Tabuada de um numero'.center(40,'='))
# n = int(input('Escreva um numero: '))
# print(f'Tabuada do {n}'.center(40,'='))
# for c in range(1,11):
#     res = c * n
#     print(f'{c} x {n:2} = {res}'.center(40))
# print('='*40)

""" Resolução Curso em Video """
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} x {c:2} = {num * c}')