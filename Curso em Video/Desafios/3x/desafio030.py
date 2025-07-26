from contextlib import nullcontext

n = int(input('Escreva um numero: '))
print(f'A analisar o numero {n}')
if n % 2 == 0:
    print('O seu numero é Par!')
else:
    print('O seu numero é Impar!')