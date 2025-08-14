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
# from datetime import date
# pessoa = {}

# pessoa["nome"] = input("Nome: ").strip().capitalize()
# pessoa["idade"] = date.today().year - int(input("Ano de Nascimento: "))
# pessoa["CTPS"] = input("Carteira de Trabalho (0 se não tiver): ")
# if int(pessoa["CTPS"]) != 0:
#     pessoa["contratação"] = int(input("Ano de contratação: "))
#     pessoa["salário"] = int(input("Salário: R$ "))
#     pessoa["aposentadoria"] =  pessoa["contratação"] + 35 - date.today().year + pessoa["idade"]
# print("-=" * 25 + "-")
# for k, v in pessoa.items():
#     print(f"{k} tem o valor {v}")

""" Resolução Curso em Video """
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')