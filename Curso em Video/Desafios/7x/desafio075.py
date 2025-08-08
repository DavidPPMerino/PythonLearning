""" Enunciado:
Desenvolva um programa que leia 'quatro valores' pelo 'teclado' e guarde-os em
uma 'tupla'. No final, mostre:
a) Quantas vezes apareceu o valor '9'.
b) Em que posição foi digitado o primeiro valor '3'.
c) Quais foram os números pares.
"""

" V1.0 "
n1 = int(input("Escreva um número: "))
n2 = int(input("Escreva outro número: "))
n3 = int(input("Escreva mais um número: "))
n4 = int(input("Escreva um ultimo número: "))
t = n1, n2, n3, n4
print(f"Os valores digitados foram: {t}")
print(f"O valor 9 {"apareceu" if 9 in t else "não apareceu"} {"nenhuma" if t.count(9) < 1 else t.count(9)} {"vez." if t.count(9) < 2 else "vezes."}")
print(f" O valor 3 {"não apareceu" if 3 not in t else "apareceu na"} {t.index(3)+1 if 3 in t else ""}{"ª posição." if 3 in t else "em nenhuma posição."}")
print('Os números pares escritos foram: ', end='')
for i, num in enumerate(t):
    if num != 0:
        if num % 2 == 0:
            if i == 0:
                print(num, end='')
            else:
                print(", ",num, end='')
    else:
        print("nenhum número par encontrado.")

""" Resolução Curso em Video """
núm = (int(input("Escreva um número: ")),
       int(input("Escreva outro número: ")),
       int(input("Escreva mais um número: ")),
       int(input("Escreva um ultimo número: ")))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {núm.count(9)} vezes')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')