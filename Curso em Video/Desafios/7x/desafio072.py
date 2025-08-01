"""Enunciado:
Crie um programa que tenha uma 'tupla' totalmente preenchida com uma contagem por extenso, de 'zero' até 'vinte'.
Seu programa deverá ler um número pelo teclado('entre 0 e 20') e mostrá-lo por extenso.
"""

nums = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "catorze",
    "quinze",
    "dezasseis",
    "dezassete",
    "dezoito",
    "dezanove",
    "vinte",
)
num = -1
while not (0 <= num < 20):
    num = int(input("Escreva um número entre 0 e 20: "))
print(f"Você escreveu o número {nums[num]}")
