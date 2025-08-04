""" Enunciado:
Faça um programa que leia '5 valores numéricos'e guarde-os em uma 'lista'.
No final, mostre qual foi o 'maior' e o 'menor' valor digitado e as suas 
respetivas 'posições' na lista.
"""
list = []
for count in range(0, 5):
    list.append(int(input(f"Escreva um valor para a Posição {count}: ")))
print('-=' * 15 + '-')
print(f"Você escreveu os valores {list}")
print(f"O maior valor digitado foi {max(list)} {'nas posições' if list.count(max(list)) > 1 else 'na posição'}", end=" ")
for i, num in enumerate(list):
    if num == max(list):
        print(f'{i}... ', end=' ')
print(f"\nO menor valor digitado foi {min(list)} {'nas posições' if list.count(min(list)) > 1 else 'na posição'}", end=" ")
for i, num in enumerate(list):
    if num == min(list):
        print(f"{i}... ", end=" ")
