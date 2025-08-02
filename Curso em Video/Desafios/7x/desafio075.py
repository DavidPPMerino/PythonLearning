""" Enunciado:
Desenvolva um programa que leia 'quatro valores' pelo 'teclado' e guarde-os em
uma 'tupla'. No final, mostre:
a) Quantas vezes apareceu o valor '9'.
b) Em que posição foi digitado o primeiro valor '3'.
c) Quais foram os números pares.
"""
n1 = int(input("Escreva um número: "))
n2 = int(input("Escreva outro número: "))
n3 = int(input("Escreva mais um número: "))
n4 = int(input("Escreva um ultimo número: "))
t = n1, n2, n3, n4
print(f"O valor 9 apareceu {"nenhuma" if t.count(9) < 1 else t.count(9)} {"vez" if t.count(9) < 2 else "vezes"}")
print(f" O valor 3 {"não apareceu" if (t.find(3)+1) < 1 else "apareceu"} na {}")