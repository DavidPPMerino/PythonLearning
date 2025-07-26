import emoji
kmh = int(input('A que velocidade circulava? '))
if kmh > 80:
    print(emoji.emojize(f':police_officer::police_car: A policia apanhou-te em excesso de velocidade, como ias {kmh}Km/h a multa vai ser de {(kmh-80)*7:.2f}€'))
else:
    print(emoji.emojize(f'Parabéns por seres um condutor exemplar, circulavas a {kmh}Km/h, leva esta medalha como agradecimento :sports_medal:'))