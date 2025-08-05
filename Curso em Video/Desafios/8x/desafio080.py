""" Enunciado:
Crie um programa onde o usuário possa digitar 'cinco valores numéricos' e 
cadastre-os em uma 'lista', 'já na posição correta' de inserção (sem usar o 
'sort()').
No final, mostre a 'lista ordenada' na tela."""
nums = []
for _ in range(5):
    new = int(input("Digite um valor: "))
    if len(nums) == 0:
        nums.append(new)
    else:
        for loc, num in enumerate(nums):
            if new < num:
                nums.insert(loc, new)
                break
            else:
                nums.append(new)
                break
print(nums)
