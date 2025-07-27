""" Enunciado:
        Desenvolva um programa que leia 'seis números inteiros e mostre a soma
        apenas daqueles que forem 'pares'. Se o valor digitado for ímpar,
        desconsidere-o.
"""

" V1.0 "
# s = 0
# for c in range(0,6):
#     n = int(input('Escreva um numero inteiro: '))
#     if n % 2 == 0:
#         s += n
# print(s)

""" Resolução Curso em Video """
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Vpcê informou {cont} números PARES e a soma foi {soma}')