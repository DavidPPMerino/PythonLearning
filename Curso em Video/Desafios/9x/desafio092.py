""" Enunciado:
Crie um programa que leia 'nome', 'ano de nascimento' e 'carteira de trabalho'
e cadastre-os (com 'idade') em um 'dicionário' se por acaso a 'CTPS' for
diferente de 'ZERO', o dicionário receberá também o 'ano de contratação' e o 
'salário'.
Calcule e acrescente, além da 'idade', com quantos anos a pessoa vai se 
'aposentar'.
35 anos colaboração
"""

" V1.0 "
from datetime import date
pessoa = {}

pessoa["nome"] = input("Nome: ").strip().capitalize()
pessoa["idade"] = date.today().year - int(input("Ano de Nascimento: "))
pessoa["CTPS"] = input("Carteira de Trabalho (0 se não tiver): ")
if int(pessoa["CTPS"]) != 0:
    pessoa["contratação"] = int(input("Ano de contratação: "))
    pessoa["salário"] = int(input("Salário: R$ "))
    pessoa["aposentadoria"] =  pessoa["contratação"] + 35 - date.today().year + pessoa["idade"]
print("-=" * 25 + "-")
for k, v in pessoa.items():
    print(f"{k} tem o valor {v}")
