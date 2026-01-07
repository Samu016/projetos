import uteis
uteis.titulo('Feira da 8')

total = mais1000 = barato = cont = 0
produto_barato = ''
while True:
    cont += 1
    uteis.linha()
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: '))
    uteis.linha()
    total += preco
    if preco > 1000:
        mais1000 += 1
    if cont == 1:
        barato = preco
    if preco < barato:
        barato = preco
        produto_barato = produto
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
    elif opcao not in 'SN':
        while opcao not in 'SN':
            uteis.notas()
            opcao = str(input('Digite uma opcao válida: [S/N] ')).upper().strip()[0]
uteis.linha()
print(f'''O total de produtos digitados foi: \033[34m{total:.2f} reais\033[m.
O produto mais barato foi \033[34m{produto_barato}\033[m, custando \033[34m{barato:.2f} reais\033[m.
Houve \033[34m{mais1000}\033[m produtos com mais de \033[34m1000 reais\033[m.
''')