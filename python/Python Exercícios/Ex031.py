viagem = int(input('Qual a distância da viagem? '))
if viagem <= 200:
    print(f'Sua viagem vai custar {viagem*0.5:.2f} reais.')
else:
    print(f'PROMOÇÃO! Sua viagem vai custar {viagem*0.45:.2f} reais.')