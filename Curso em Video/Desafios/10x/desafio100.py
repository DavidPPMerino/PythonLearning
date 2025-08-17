""" Enunciado:
Faça um programa que tenha uma 'lista' chamada 'números' e duas 'funções' 
chamadas 'sorteia()' e 'somaPar().
A primeira função vai sortear '5 números' e vai colocá-los dentro da lista e a 
segunda função vai mostrar a 'soma' entre todos os valores 'pares' sorteados 
pela função anterior.
"""

" V1.0 "
from random import randint
from time import sleep

def sorteia(a):
    print('Sorteando 5 valores da lista:', end=' ')
    for i in range(5):
        a.append(randint(1, 10))
        print(f'{a[-1]}', end=' ', flush=True)
        sleep(0.4)
    print('Pronto!')
def somaPar(a):
    soma = 0
    for num in a:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {a}, temos {soma}')

numeros = []
sorteia(numeros)
somaPar(numeros)