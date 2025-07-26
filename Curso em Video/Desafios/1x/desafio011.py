""" Enunciado:
        Faça um programa que leia a largura e a altura de uma parede em metros,
        calcule a sua área e a quantidade de tinta necessária para pintã-la,
        sabendo que cada litro de tinta, pinta uma área de 2m²
"""

" V1.0 "
# print('===== Calculadora de pintura =====')
# a = float(input('Qual é a largura da parede em metros: '))
# l = float(input('Qual é a altura da parede em metros: '))
# m2 = a*l
# Lt = m2/2
# print('Uma parede com {} metros de altura e {} metros de largura tem uma area de {} e irá precisar aproximadamente de {} litros de tinta'.format(a, l, m2, Lt))

""" Resolução Curso em Video """
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print(f'Sua parede tem a dimensão de {larg}x{alt} e a sua área é de {área}m².')
tinta = área / 2
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta.')