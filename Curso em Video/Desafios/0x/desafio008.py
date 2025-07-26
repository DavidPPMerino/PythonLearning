""" Enunciado:
        Escreva um programa que leia um valor em metros e o exiba em
        centímetros e milímetros.
"""

" V1.0 "
# print('===== Conversor de metros para centimetros e milimetro')
# n = float(input('Quantos metros quer converter: '))
# cm = n*100
# mm = n*1000
# print('A conversão de {} metros equivale a {} centimetros e {} milimetros'.format(n, cm, mm))

""" Resolução Curso em Video """
medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida}m corresponde a {cm:.0f}cm e {mm:.0f}mm')

" Desafiou a mostrar km hm dam m dm cm mm"