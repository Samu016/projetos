import uteis
uteis.titulo('Media, maior e menor')

usuario = int(input('Digite um número: '))
opcao = ''
maior = menor = ant = cont = soma = 0
maior = menor = usuario
while opcao != 'N':
    cont += 1
    if cont > 1:
        ant = usuario
        usuario = int(input('Digite um número: '))
    soma += usuario
    media = soma / cont
    if usuario > maior:
        maior = usuario
    elif usuario < menor:
        menor = usuario
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()
    if opcao != 'N' and opcao != 'S':
        uteis.notas()
        break
print(f'''
O maior número digitado foi: {maior}.
O menor número digitado foi: {menor}.
A média é {media:.2f}.
''')
