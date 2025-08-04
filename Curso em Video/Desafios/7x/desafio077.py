""" Enunciado:
Crie um programa que tenha uma 'tupla' com 'várias palavras' (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas 'vogais'.
"""
words = "aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro"
vowels = "a", "e", "i", "o", "u"
for word in words:
    print(f"Na palavra {word.upper()} temos ", end='')
    for letter in word:
        if letter in vowels:
            print(f"{letter} ", end='')
    print()