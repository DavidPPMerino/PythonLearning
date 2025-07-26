a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(a1, a1+r*10, r):
    print(c, end=' ')