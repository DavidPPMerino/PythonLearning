""" Enunciado:
        Faça um programa que leia três números e mostre qual é o maior
        e qual é o menor.
"""

" V1.0 "
# n1 = int(input('Escreva o primeiro numero: '))
# n2 = int(input('Escreva o segundo numero: '))
# n3 = int(input('Escreva o terceiro numero: '))
# print(f'maior: {max(n1, n2, n3)}, menor: {min(n1, n2, n3)}')

""" Resolução Curso em Video """
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')