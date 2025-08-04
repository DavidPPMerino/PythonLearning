""" Enunciado:
Crie um programa que tenha uma 'tupla' com 'várias palavras' (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas 'vogais'.
"""
# words = "aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro"
# vowels = "a", "e", "i", "o", "u"
# for word in words:
#     print(f"Na palavra {word.upper()} temos ", end='')
#     for letter in word:
#         if letter in vowels:
#             print(f"{letter} ", end='')
#     print()

""" Resolução Curso em Video """
palavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis", 
            "estudar", "praticar", "trabalhar", "mercado", "programador", 
            "futuro")
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')