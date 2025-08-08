"""Enunciado:
Crie um programa que tenha uma 'tupla' totalmente preenchida com uma contagem por extenso, de 'zero' até 'vinte'.
Seu programa deverá ler um número pelo teclado('entre 0 e 20') e mostrá-lo por extenso.
"""

" V1.5 Adicionado verificação de continuação"
nums = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", 
        "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze",
        "dezasseis", "dezassete", "dezoito", "dezanove", "vinte")
while True:
    num = -1
    while not (0 <= num < 20):
        num = int(input("Escreva um número entre 0 e 20: "))
    print(f"Você escreveu o número {nums[num].capitalize()}")
    while True: 
        check = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if check in ("S", "N"):
            break
    if check in "N":
            break
" V1.0 "
# nums = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", 
        # "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze",
        # "dezasseis", "dezassete", "dezoito", "dezanove", "vinte")
# num = -1
# while not (0 <= num < 20):
#     num = int(input("Escreva um número entre 0 e 20: "))
# print(f"Você escreveu o número {nums[num]}")

""" Resolução Curso em Video """
# cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", 
#         "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze",
#         "dezasseis", "dezassete", "dezoito", "dezanove", "vinte")
# while True:
#     núm = int(input('Digite um número entre 0 e 20: '))
#     if 0 <= núm <= 20:
#         break
#     print('Tente novamente. ',end='')
# print(f'Você digitou o número {cont[num]}')