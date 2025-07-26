print('\033[1;31m-'*10,'\033[4;33mConversor de Números\033[m','\033[1;31m-\033[m'*10)
num1 = int(input('\033[0;33mEscreva um número inteiro: '))
print('\033[1;31m-'*42)
num2 = int(input('\033[0;33mEscreva outro número inteiro: '))
print('\033[1;31m-'*42)

print('\033[1;31m-'*10,'\033[33mNúmeros selecionados\033[m','\033[1;31m-\033[m\033[1;31m'*10)
print(f' \033[1;4;33m{num1}\033[m \033[1;31m||\033[m \033[1;4;33m{num2}\033[m \033[1;31m'.center(83,'.'))
print('')
if num1 > num2:
    print(f'\033[33mO \033[31m{num1} \033[33mé o maior dos números!')
elif num1 < num2:
    print(f'\033[33mO \033[31m{num2} \033[33mé o maior dos números!')
else:
    print(f'\033[33mAmbos os números são \033[31miguais\033[33m!')
