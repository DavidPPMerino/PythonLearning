num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
# num[4] = 7 # IndexError: list assignment index out of range
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.insert(2, 0)
print(num)
num.pop
print(num)
num.pop(3)
num.remove(2) # remove o primeiro 2 da lista

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end='')

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a 
b[2] = 8 # Muda nas duas listas porque o python cria uma ligação ao igualar 2 listas
print(f'Lista A: {a}')
print(f'Lista B: {b}')
b = a[:] # aqui sim cria uma copia sem ligação