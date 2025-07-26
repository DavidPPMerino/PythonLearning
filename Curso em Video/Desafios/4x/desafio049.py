print('Tabuada de um numero'.center(40,'='))
n = int(input('Escreva um numero: '))
print(f'Tabuada do {n}'.center(40,'='))
for c in range(1,11):
    res = c * n
    print(f'{c} x {n} = {res}'.center(40))
print('='*40)
