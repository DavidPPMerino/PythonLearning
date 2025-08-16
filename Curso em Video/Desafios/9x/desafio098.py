""" Enunciado:
Faça um programa que tenha uma 'função' chamada 'contador()', que receba três
'parâmetros': 'início', 'fim' e 'passo' e realize a contagem.
Seu programa tem que realizar 'três contagens' através da função criada:
a) De '1' até '10', de '1' em '1'
b) De '10' até '0', de '2' em '2'
c) Uma contagem 'personalizada'.
"""

" V1.0 "
from time import sleep
def mostraLinha():
    print('-=' * 25 + '-')

def contador(a, b, c):
    mostraLinha()
    if c == 0:
        c = 1
    print(f'Contagem de {a} até {b} de {abs(c)} em {abs(c)}')
    if a > b and c > 0:
        c = -c
    if a < b:
        b += 1
    elif a > b:
        b -= 1

    for i in range(a, b, c):
        print(f'{i} ', end='', flush=True)
        sleep(0.2)
    print('FIM!')

def titulo(txt):
    print('-=' * 25 + '-')
    print(txt.center(51))
    print('-=' * 25 + '-')

contador(1, 10, 1)
contador(10, 0, 2)
titulo('Agora é a tua vez de personalizar a contagem!')   
i = int(input('Início: '))
f = int(input('Fim: '.ljust(8)))
p = int(input('Passo: '.ljust(8)))
contador(i, f, p)
