""" Enunciado:
Faça um programa que tenha uma 'função' chamada 'maior()', que receba vários
'parâmetros' com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o 'maior'.
"""

" V1.0 "
from time import sleep
def mostraLinha():
    print('-=' * 25 + '-')

def maior(* n):
    mostraLinha()
    print('Analisando os valores passados...')
    if len(n) > 0:
        for x in n:
            print(f'{x} ', end='', flush=True)
            sleep(0.3)
    
    print(f'Foram informados {len(n)} valores ao todo.')
    print(f'O maior valor informado foi {max(n) if len(n) > 0 else 0}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()