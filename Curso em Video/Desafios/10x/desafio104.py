""" Enunciado:
Crie um programa que tenha a 'função' 'leiaInt()', que vai funcionar de forma
semelhante à função 'input()' do Python, só que fazendo a 'validação' para 
aceitar apenas um valor numérico.

Ex:
n = leiaInt('Digite um n')
"""

" V1.0 "
def leiaInt(txt):
    while True:
        n = input(txt)
        if not n.isdigit():
            print('\033[1;31m ERRO! Digite um número inteiro válido.\033[m')
        else:
            break
    return n


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')