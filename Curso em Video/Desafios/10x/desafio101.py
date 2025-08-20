""" Enunciado: 
Crie um programa que tenha uma 'função' chamada 'voto()' que vai receber como
'parâmetro' o 'ano de nascimento' de uma pessoa, 'retornando' um valor 'literal' indicando se uma pessoa tem voto 'negado', 'opcional' ou 'obrigatório' nas eleições.
negado < 18
opcional > 65
obrigatorio else
"""

" V1.0 "
def voto(birth):
    from datetime import date
    global age
    age = date.today().year - birth
    if age < 18:
        return "NÃO VOTA"
    elif age > 65:
        return "VOTO OPCIONAL"
    else:
        return "VOTO OBRIGATÓRIO"
    

age = 0
resp = int(input("Em que ano você nasceu? "))
votos = voto(resp)
print(f"Com {age} anos: {votos}")
