"""Enunciado:
Crie um programa que vai ler 'vários números' e colocar em uma 'list'.
Depois disso, mostre:
a) 'Quantos' números foram digitados.
b) A lista de valores, ordenada de forma 'decrescente'.
c) Se o valor '5' foi digitado e está ou não na 'lista'.
"""

nums = []
while True:
    check = " "
    nums.append(int(input("Digite um valor: ")))
    while check not in "SN":
        check = str(input("Deseja continuar? [S/N]")).upper().strip()[0]
    if check == "N":
        break
nums.sort(reverse=True)
print("-=" * 15 + "-")
print(f"Você escreveu {len(nums)} elementos.")
print(f"Os valores em ordem decrescente são {nums}")
if 5 in nums:
    print("O valor 5 foi encontrado na lista!")
else:
    print("O valor 5 não foi encontrado na lista!")

""" Resolução Curso em Video """
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
