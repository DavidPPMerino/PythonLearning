""" Enunciado:
Faça um programa que tenha uma 'função' chamada 'contador()', que receba três
'parâmetros': 'início', 'fim' e 'passo' e realize a contagem.
Seu programa tem que realizar 'três contagens' através da função criada:
a) De '1' até '10', de '1' em '1'
b) De '10' até '0', de '2' em '2'
c) Uma contagem 'personalizada'.
"""

" V1.0 "
# from time import sleep
# def mostraLinha():
#     print('-=' * 25 + '-')
# def titulo(txt):
#     print('-=' * 25 + '-')
#     print(txt.center(51))
#     print('-=' * 25 + '-')
# def contador(a, b, c):
#     mostraLinha()
#     if c == 0:
#         c = 1
#     print(f'Contagem de {a} até {b} de {abs(c)} em {abs(c)}')
#     if a > b and c > 0:
#         c = -c
#     if a < b:
#         b += 1
#     elif a > b:
#         b -= 1

#     for i in range(a, b, c):
#         print(f'{i} ', end='', flush=True)
#         sleep(0.2)
#     print('FIM!')


# # Programa
# contador(1, 10, 1)
# contador(10, 0, 2)
# titulo('Agora é a tua vez de personalizar a contagem!')   
# i = int(input('Início: '))
# f = int(input('Fim: '.ljust(8)))
# p = int(input('Passo: '.ljust(8)))
# contador(i, f, p)

""" Resolução Curso em Video """
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)