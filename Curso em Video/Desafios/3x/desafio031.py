km = int(input('Qual a distancia em km da sua viagem?: '))
if km <=200:
    print(f'O preço da viagem para {km} é de {km*0.5:.2f}€')
else:
    print(f'O preço da viagem para {km} é de {km*0.45:.2f}€')