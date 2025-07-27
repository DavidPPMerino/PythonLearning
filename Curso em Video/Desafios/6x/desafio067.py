""" Enunciado:
        Faça um programa que mostre a 'tabuada' de 'vários números', um
        de cada vez, para cada valor digitado pelo usuário.
        O programa será 'interrompido' quando o número solicitado
        for 'negativo'.
"""

" V1.0 "

while True:

    print('-' * 50)
    n = int(input('Qual tabuada deseja ver? '))
    print('-' * 50)

    if n < 0:
        print(f'PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break

    for x in range(1, 11):
        r = n * x
        print(f'{n} x {x:2} = {r}')
