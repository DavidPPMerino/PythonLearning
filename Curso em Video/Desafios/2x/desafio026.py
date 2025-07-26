frase = input('Escreva uma frase: ').strip().lower()
print(f'''A letra "a" aparece {frase.count('a')} vezes na frase.
A letra "a" aparece pela primeira vez na frase na posição {frase.find('a')+1}
A letra "a" aparece pela ultima vez na frase na posição {frase.rfind('a')+1}''')