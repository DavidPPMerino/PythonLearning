""" Enunciado:
        Desenvolva um programa que leia o 'primeiro termo' e a 'razão' de uma PA.
        No final, mostre os '10' primeiros termos dessa Progressão Aritmetica.
"""

" V1.0 "
# a1 = int(input('Primeiro termo: '))
# r = int(input('Razão: '))
# for c in range(a1, a1+r*10, r):
#     print(c, end=' ')

""" Resolução Curso em Video """
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1 ) * razão
for c in range(primeiro, décimo + razão, razão):
    print(f'{c} ', end='→ ')
print('ACABOU')