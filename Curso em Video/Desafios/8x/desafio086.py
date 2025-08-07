""" Enunciado:
Crie um programa que crie uma 'matriz' de 'dimensão 3x3' e preencha com valores
lidos pelo teclado.
No final, mostre a 'matriz' na tela, com a formatação correta.
[ 1 ][ 2 ][ 3 ]
[ 4 ][ 5 ][ 6 ]
[ 7 ][ 8 ][ 9 ]
"""

"V1.0"
# matrix = [[], [], []]
# for col, line in enumerate(matrix):
#     for i in range(0, 3):
#         num = int(input(f"Escreva um valor para [{col}, {i}]: "))
#         matrix[col].insert(i, num)
# print("-=" * 20 + "-")
# for line in matrix:
#     for num in line:
#         print(f"[ {num} ]", end="")
#     print()

""" Resolução Curso em Video """
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
    