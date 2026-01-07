import random, uteis, time
uteis.titulo('Jogo de Advinhação')

resposta = random.randint(0, 10)
jogador = int(input('Escolha um numero entre 0 e 10: '))
palpite = 0
while jogador != resposta:
    jogador = int(input('\033[31mERROU!\033[m Tente novamente: '))
    palpite += 1
print(f'Você acertou, o número era {resposta}.\nForam necessários {palpite} palpites.')
