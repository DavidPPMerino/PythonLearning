n1 = int(input('Escreva um valor: '))
n2 = int(input('Escreva outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
rd = n1 % n2
print('A soma entre {} e {} é {}, \n a divisão é {}, \n o produto é {}'.format(n1, n2, s, d, m), end='\n >>><<< \n')
print(' A divisão inteira é {}, \n o resto da divisão é {} \n e a potência é {}'.format(di, rd, e))

