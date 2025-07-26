""" Enunciado:
        Escreva um programa que converta uma temperatura digitada
        em ºC e converta para ºF.
"""

" V1.0 "
# print('='*10," Conversor de temperaturas", '='*10)
# c = float(input('Escreva a temperatura em ºC: '))
# cc = c*1.8+32
# print('A conversão de {:.2f}ºC são {:.2f}ºF.'.format(c,cc))
#
# f = float(input('Escreva a temperatura em Fahrenheit: '))
# cf = (f-32)/1.8
# print('A conversão de {:.2f}ºF são {:.2f}ºC'.format(f,cf))

""" Resolução Curso em Video """
c= float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32
print(f'A temperatura de {c}ºC corresponde a {f}ºF!')