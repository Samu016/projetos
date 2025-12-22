from random import randint
aleatorio = randint(0, 5)
jogador = int(input("Escolha um numero de 0 a 5: "))
if jogador == aleatorio:
    print('PARABÉNS! VC VENCEU!')
else:
    print(f'VC PERDEU! O número era {aleatorio}')
