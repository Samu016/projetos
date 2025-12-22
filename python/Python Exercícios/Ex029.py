velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print(f'Vc excedeu o limite de velocidade! Vc tem que pagar {(velocidade-80)*7} reais de multa.')
else:
    print('Pode prosseguir!')