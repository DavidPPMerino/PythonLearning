""" Enunciado:
        Desenvolva um programa que leia o comprimento de três retas e diga
        ao usuário se elas podem ou não formar um triângulo.
"""

" V1.0 "
# r1 = float(input('Escreva o tamanho da primeira reta: '))
# r2 = float(input('Escreva o tamanho da segunda reta: '))
# r3 = float(input('Escreva o tamanho da terceira reta: '))
# if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
#     print('Sim é possivel criar um triangulo!')
# else:
#     print('Infelizmente não é possivel criar um triangulo!')

""" Resolução Curso em Video """
print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triãngulo')