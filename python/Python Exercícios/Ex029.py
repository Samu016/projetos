print('\033[33m=+\033[m' * 20)
print('\033[1;34mRADAR DE TRÂNSITO')
print('\033[33m=+\033[m' * 20)

velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print(f'Vc excedeu o limite de velocidade! Vc tem que pagar {(velocidade-80)*7} reais de multa.')
else:
    print('Pode prosseguir!')