""" Enunciado:
Crie um programa onde o usuário possa digitar 'sete valores numéricos' e 
cadastre-os em uma 'lista única' que mantenha separados os valores 'pares' e 
'ímpares'.
No final, mostre os valores pares e ímpares em ordem 'crescente'.
"""

nums = [[],[]]
for _ in range(1, 8):
    num = int(input("Escreva um valor: "))
    if not num % 2:
        nums[0].append(num)
    else:
        nums[1].append(num)
nums[0].sort()
nums[1].sort()
print("-=" * 20 + "-")
print(f"Os valores pares escritos foram: {nums[0]}")
print(f"Os valores ímpares escritos foram: {nums[1]}")

""" Resolução Curso em Video """
