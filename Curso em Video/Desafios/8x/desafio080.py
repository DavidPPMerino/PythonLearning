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
                print(f"Adicionado na posição {loc} da lista...")
                break
            else:
                nums.append(new)
                print("Adicionado ao final da lista...")
                break
print("-=" * 15 + "-")
print(f"Os valores digitados em ordem foram {nums}")

""" Resolução Curso em Video """
lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado a posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em orgem foram {lista}')