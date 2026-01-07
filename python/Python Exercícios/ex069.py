import uteis
uteis.titulo('Idade e sexo')

maioridade = sexoM = menorF = 0
while True:
    uteis.linha()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if sexo not in 'MF':
        while sexo not in 'MF':
            uteis.notas()
            sexo = str(input('Digite uma opção válida: [M/F] ')).upper().strip()[0]
    uteis.linha()
    print('\033[33mRegistrado com sucesso!\033[m')
    if idade >= 18:
        maioridade += 1
    if sexo == 'M':
        sexoM += 1
    if sexo == 'F' and idade < 20:
        menorF += 1
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
    elif opcao not in 'SN':
        while opcao not in 'SN':
            uteis.notas()
            opcao = str(input('Digite uma opção válida: [S/N] ')).upper().strip()[0]

uteis.linha()
print(f'''Há {maioridade} maiores de idade registrados.
Há {sexoM} homens registrados.
Há {menorF} mulheres com menos de 20 anos registrados.
''')