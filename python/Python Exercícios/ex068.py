import uteis
from random import randint
uteis.titulo('Par ou ímpar')

c = 0
while True:
    uteis.linha()
    usuario = str(input('Escolha ímpar ou par: [P/I] ')).upper().strip()[0]
    if usuario not in 'PI':
        while usuario not in 'PI':
            uteis.notas()
            usuario = str(input('Digite uma opcao válida [P/I] ')).upper().strip()[0]
    pc = randint(1, 10)
    us = int(input('Diga um numero de 1 a 10: '))
    uteis.linha()
    soma = us + pc
    print(f'Eu escolhi {pc} e vc {us} e a soma deu {soma}.')
    if usuario == 'P':
        if soma % 2 == 0:
            print('\033[34mParabéns!\033[m O resultado foi\033[34m Par\033[m')
            c += 1
        else:
            print('\033[31mVocê perdeu!\033[m O resultado foi\033[31m Ímpar\033[m')
            break
    elif usuario == 'I':
        if soma % 2 != 0:
            print('\033[34mParabéns, você ganhou!\033[m O resultado foi\033[34m Ímpar\033[m')
            c += 1
        else:
            print('\033[31mVocê perdeu!\033[m O resultado foi\033[31m Par\033[m')
            break

print(f'\033[1;32mFIM\033[m. Você venceu {c} vezes.')
