""" Enunciado:
        Faça um programa que mostre a 'tabuada' de 'vários números', um
        de cada vez, para cada valor digitado pelo usuário.
        O programa será 'interrompido' quando o número solicitado
        for 'negativo'.
"""

" V1.0 "

# while True:

#     print('-' * 50)
#     n = int(input('Qual tabuada deseja ver? '))
#     print('-' * 50)

#     if n < 0:
#         print(f'PROGRAMA TABUADA ENCERRADO. Volte sempre!')
#         break

#     for x in range(1, 11):
#         r = n * x
#         print(f'{n} x {x:2} = {r}')

""" Resolução Curso em Video """
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')