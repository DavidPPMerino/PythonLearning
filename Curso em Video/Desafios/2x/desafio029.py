""" Enunciado:
        Escreva um programa que leia a velocidade de um carro.
        Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
        que ele foi multado.
        A multa vai custar R$7,00 por cada Km acima do limite.
"""

" V1.0 "
# import emoji
# kmh = int(input('A que velocidade circulava? '))
# if kmh > 80:
#     print(emoji.emojize(f':police_officer::police_car: A policia apanhou-te em excesso de velocidade, como ias {kmh}Km/h a multa vai ser de {(kmh-80)*7:.2f}€'))
# else:
#     print(emoji.emojize(f'Parabéns por seres um condutor exemplar, circulavas a {kmh}Km/h, leva esta medalha como agradecimento :sports_medal:'))

""" Resolução Curso em Video """
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')