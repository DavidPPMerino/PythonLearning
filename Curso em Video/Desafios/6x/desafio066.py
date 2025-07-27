""" Enunciado:
        Crie um programa que leia 'vários números inteiros pelo teclado.
        O programa só vai parar quando o usuário digitar o valor '999', que
        é a 'condição de parada'.
        No final, mostre 'quantos números' foram digitados e qual foi a 'soma'
        entre eles (desconsiderando o flag).
        EX:
        A soma dos 3 valores foi 12!
"""

" V1.0 "
soma = 0
count = 0
while True:
    n = int(input('Escreva um valor (999 para parar): '))
    if n == 999:
        break
    soma += n
    count += 1
print(f'A soma dos {count} valores foi de {soma}!')