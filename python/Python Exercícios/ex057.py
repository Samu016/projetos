import uteis
uteis.titulo('apenas m/f')

sexo = str(input('Qual seu sexo? [M/F] ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    uteis.notas()
    sexo = str(input('Digite uma resposta válida: [M/F] ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')