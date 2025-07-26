from time import sleep as slp


print('\033[1;31m-'*16,'\033[4;33mContagem para Fogo de Artifício\033[m','\033[1;31m-\033[m'*17)
str(input('Carregue enter para iniciar a contagem: '))
for c in range(10, 0, -1):
    print(f'{c:^40}')
    slp(1)
print('Bum Bum Bum')