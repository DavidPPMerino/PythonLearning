from time import sleep as slp
from datetime import date
curyear = date.today().year

print('\033[1;31m-'*10,'\033[4;33mCalculadora de Alistamento\033[m','\033[1;31m-\033[m'*10)
birth = int(input('\033[0;33mEscreva o seu ano de nascimento: '))
idd = curyear - birth

print('\033[1;31m-'*48)
print(f'A analisar a sua idade...'.center(42),'\033[m')
slp(1)

print('\033[1;4;31;43m','Categoria Calculada'.center(41),'\033[m')
slp(1)

# if idd <= 9:
if idd <= 9:
    print(f'A sua idade é {idd} e irá competir na categoria: Mirim')

# elif 14 >= idd > 9:
elif idd <= 14:
    print(f'A sua idade é {idd} e irá competir na categoria: Infantil')

# elif 19 >= idd > 14:
if idd <= 19:
    print(f'A sua idade é {idd} e irá competir na categoria: Junior')

# elif 25 >= idd > 19:
if idd <= 25:
    print(f'A sua idade é {idd} e irá competir na categoria: Sénior')

else:
    print(f'A sua idade é {idd} e irá competir na categoria: Master')
