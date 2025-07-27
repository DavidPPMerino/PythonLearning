""" Enunciado:
        Desenvolva um programa que pergunte a distância de uma viagem em Km.
        Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de
        até 200Km e R$0.45 para viagens mais longas.
"""

" V1.0 "
# km = int(input('Qual a distancia em km da sua viagem?: '))
# if km <=200:
#     print(f'O preço da viagem para {km} é de {km*0.5:.2f}€')
# else:
#     print(f'O preço da viagem para {km} é de {km*0.45:.2f}€')

""" Resolução Curso em Video """
distância = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distância}Km.')
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print(f'E o preço da sua passagem será de R${preço:.2f}')