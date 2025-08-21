""" Módulos e Pacotes """

" Modularização "

# → Surgiu na decada de 60
# → Sistemas cada vez maiores
# → Foco: dividir um programa grande
# → Foco: Aumentar a legibilidade
# → Foco: Facilitar a manutenção

# import uteis

# num = int(input('Digite um valor: '))
# fat = uteis.fatorial(num)
# print(f'O fatorial de {num} é {fat}')
# print(f'O dobro de {num} é {uteis22.dobro(num)}')

" posso passar as funções criadas e passar para outro ficheiro na mesma pasta e importar esse ficheiro com as funções."

from uteis22 import fatorial, dobro

num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')

# Não é aconselhado utilizar este tipo de importação porque pode criar conflitos se houver importação de outro módulo que tambem tenha a mesma função.
# Por exemplo se importar o dobro() e importar outro módulo que tambem tenho dobro() a que prevalece é a ultima importada.

" Vantagens"

# → Organização do código
# → Facilidade na manutenção
# → Ocultação de código detalhado
# → Reutilização em outros projetos

""" Pacotes / Bibliotecas """

# Pacote uteis

# Números           # Strings
# def kjlk():        # def asoi():   
# def adsa():        # def oiie():
# def asko():
# def klahsi():


# Datas             # Cores
# def laius():       # def qoije():
# def asujça():      # def aouha():
# def epioan():      # def qpowi():
# def qp+pd():       # def poqwi():
# def çhaoud():      # def fskjf():
# def aihnd():
# def qopei():


# Exemplo do pacote uteis com diversos modulos:
# Números, Strings, Datas, Cores.

from uteis import datas
import Desafios

# O pacote é basicamente uma pasta com os modulos lá dentro

#   📂uteis
#     | __init__.py         # pasta do pacote pode ter init
#     ↳ 📂cores
#     |     __init__.py
#     ↳ 📂datas
#     |     __init__.py
#     ↳ 📂números
#     |     __init__.py
#     ↳ 📂strings
#           __init__.py