""" Enunciado:

"""

" V1.0 "
# frase = str(input('Escreva uma frase: ')).strip()
# fraselimpa = frase.lower().replace(' ', '')
#
# if fraselimpa == fraselimpa[::-1]:
#     print(f'''A frase:
# {frase}
# é um palíndromo!''')
#
# else:
#     print(f'''A frase:
#             {frase}
#             não é um palíndromo!''')

""" Resolução Curso em Video com laço for """
frase = str(input('Escreva uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso+= junto[letra]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é palíndromo!')

""" Resolução Curso em Video sem laço for """
frase = str(input('Escreva uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é palíndromo!')