from time import sleep as slp

print('\033[1;31m-'*10,'\033[4;33mConversor de Números\033[m','\033[1;31m-\033[m'*10)
peso = float(input('\033[0;33mEscreva a sua idade: Kg '))
print('\033[1;31m-'*42)
alt = float(input('\033[0;33mEscreva a sua altura: M '))
print('\033[1;31m-'*42)

print(f'A analisar os seus dados...'.center(42),'\033[m')
slp(1)
imc = peso / alt ** 2

print('\033[1;4;31;43m','IMC Calculado'.center(40),'\033[m\033[1;31m')
print(f' \033[1;4;33m{imc:.1f}\033[m \033[1;31m'.center(61,'.'))
slp(1)
if imc < 18.5:
    print('Você está \033[31mAbaixo do peso\033[m')
#elif imc >= 18.5 and imc < 25:
#elif 18.5 <= imc < 25:
elif imc < 25:
    print('Você está com o \033[31mPeso Ideal\033[m')
#elif imc >= 25 and imc <30:
#elif 25 <= imc < 30
elif imc < 30:
    print('Você está com \033[31mSobrepeso\033[m')
#elif imc >= 30 and imc < 40:
#elif 30 <= imc < 40
elif imc < 40:
    print('Você está com \033[31mObesidade\033[m')
else:
    print('Você está com \033[31mObesidade mórbida\033[m')