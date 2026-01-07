import uteis
uteis.titulo('menu')

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input('''
    Você deseja:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair
>>>>>>> '''))
    if opcao == 1:
        print(f'A soma é {n1 + n2}')
    elif opcao == 2:
        print(f'O produto é {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior é {n1}')
        elif n1 < n2:
            print(f'O maior é {n2}')
        else:
            print('Não existe valor maior')
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        continue
    elif opcao > 5 or opcao < 0:
        uteis.notas()
        pass
