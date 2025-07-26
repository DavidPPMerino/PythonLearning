""" Enunciado:
        Melhore o desafio 061, perguntando para o usuario se ele quer mostrar
        mais alguns termos.
        O programa encerra quando ele disser que quer mostrar 0 termos.
"""

" V1.0 "
# primeirotermo = int(input('Primeiro termo: '))
# razao = int(input('Razão: '))
# count = 1
# vezes = 1
# continuar = 1
# termos = 10
# print(primeirotermo, end=' ')
# while continuar == 1:
#     while count != termos:
#         primeirotermo += razao
#         print(primeirotermo, end= ' ')
#         count += 1
#     print('')
#
#     vezes = int(input('Quantos mais termos deseja mostrar?: '))
#     termos += vezes
#     if vezes == 0:
#         continuar = 0

""" Resolução Curso em Video """

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressao finalizada com {total} termos mostrados.')