import random, uteis
uteis.titulo('JOKENPÔ', 12)

opcao = int(input("""ESCOLHA UMA DAS OPÇÕES:
PEDRA [0]
PAPEL [1]
TESOURA [2]"""))
pc = random.randint(0, 2)

jogo = ['PEDRA', 'PAPEL', 'TESOURA']
def resultado():
    if 0 <= opcao <= 2:
        print(f'Você escolheu {jogo[opcao]} e eu escolhi {jogo[pc]}')
    else:
        uteis.notas()

if opcao == pc:
    resultado()
    print('EMPATE')
elif opcao != pc and opcao == 0 and pc == 2:
    resultado()
    print('VC VENCEU!')
elif opcao != pc and opcao == 1 and pc == 0:
    resultado()
    print('VC VENCEU!')
elif opcao != pc and opcao == 2 and pc == 1:
    resultado()
    print('VC VENCEU!')
elif 0 > opcao or opcao > 2:
    uteis.notas()
else:
    resultado()
    print('PERDEU')
