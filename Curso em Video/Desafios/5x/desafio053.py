#
#
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

frase = str(input('Escreva uma frase: ')).strip()
fraselimpa = frase.lower().replace(' ', '')
inverso = ''
for letra in range(len(fraselimpa) -1, -1, -1):
    inverso+= fraselimpa[letra]
if inverso == fraselimpa:
    print('palindromo')
else:
    print('não é palindromo')