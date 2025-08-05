""" Enunciado:
Crie um programa onde o usuário possa digitar 'cinco valores numéricos' e 
cadastre-os em uma 'lista', 'já na posição correta' de inserção (sem usar o 
'sort()').
No final, mostre a 'lista ordenada' na tela."""
list = []
# print(list[-2])
for _ in range(5):
    new = int(input("Digite um valor: "))
    if len(list) == 0:
        list.append(new)
    else:
        for loc, num in enumerate(list):
            if new < num:
                list.insert(loc, new)
                break
            else:
                list.append(new)
                break
print(list)
