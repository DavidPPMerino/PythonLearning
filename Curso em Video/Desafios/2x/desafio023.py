""" Enunciado:
        Fraça um programa que leia um número de 0 a 9999 e mostre na tela
        cada um dos dígitos separados.
        Ex:
        Digite um número: 1834
        unidade:4 dezena:3 centena:8 milhar:1
"""

" V1.0"
# n = input('Escreva um numero entre 0 e 9999: ')
#
# n1 = n.zfill(4)
#
# print(f'''----------------------
# Inseriu o numero {n}.
# ----------------------
# As unidades são: {n1[3]},
# As dezenas são {n1[2]},
# As centenas são: {n1[1]},
# e os milhares são: {n1[0]}''')
# -----------------------------------------------------
# n = int(input('Escreva um numero entre 0 e 9999: '))
#
# unidade = n // 1 % 10
# dezena = n // 10 % 10
# centena = n // 100 % 10
# milhar = n // 1000 % 10
#
# print(f"""----------------------
# Inseriu o numero {n}.
# ----------------------
# As unidades são: {unidade},
# As dezenas são {dezena},
# As centenas são: {centena},
# e os milhares são: {milhar}""")

""" Resolução Curso em Video """
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')