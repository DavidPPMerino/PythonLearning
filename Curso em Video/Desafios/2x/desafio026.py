""" Enunciado:
        Faça um programa que leia uma frase pelo teclado e mostre:
        → Quantas vezes aparece a letra 'A'.
        → Em que posição ela aparece a primeira vez.
        → Em que posição ela aparece a ultima vez.
"""

" V1.0 "
# frase = input('Escreva uma frase: ').strip().lower()
# print(f'''A letra "a" aparece {frase.count('a')} vezes na frase.
# A letra "a" aparece pela primeira vez na frase na posição {frase.find('a')+1}
# A letra "a" aparece pela ultima vez na frase na posição {frase.rfind('a')+1}''')

""" Resolução Curso em Video """
frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece{frase.count("A")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.find('A')+1}')
print(f'A última letra A apareceu na posição {frase.rfind('A')+1}')