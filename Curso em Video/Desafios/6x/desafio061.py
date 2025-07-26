""" Enunciado:
        Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
        mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

" V1.0 "
# a1 = int(input('Primeiro termo: '))
# r = int(input('Razão: '))
# count = 1
# print(a1, end= ' ')
# while count != 10:
#     a1 += r
#     print(a1, end= ' ')
#     count += 1

""" Resolução Curso em Video """
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} → ', end='')
    termo += razão
    cont += 1
print('FIM')