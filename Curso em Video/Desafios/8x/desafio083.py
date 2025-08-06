""" Enunciado:
Crie um programa onde o usuário digite uma 'expressão' qualquer que use 
'parênteses'. Seu aplicativo deverá analisar se a expressão passada está com os
parênteses abertos e fechados na 'ordem correta'.
"""
expressions = []
expressions.append(input("Escreva a expressão: "))
open = 0
close = 0
for expression in expressions:
    for char in expression:
        if char == "(":
            open += 1
        elif char == ")":
            close += 1
if open == close:
    print("Expressão valida")
else:
    print("Expressão inválida")