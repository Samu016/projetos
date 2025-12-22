nome = str(input('Digite seu nome completo: ')).strip()
silva = nome.lower().split()
for i in range(len(silva)):
    if silva[i] == 'silva':
        print('Seu nome completo tem Silva')
        break
    else:
        print('Seu nome completo não tem Silva')
        break