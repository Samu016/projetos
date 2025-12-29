import uteis
uteis.titulo('Leitura de peso')
lista_de_peso = []
for c in range(1, 6):
    peso = float(input('Digite o seu peso: '))
    lista_de_peso.append(peso)
peso_maior = max(lista_de_peso)
peso_menor = min(lista_de_peso)
print(f'O maior peso é {peso_maior} e o menor peso é {peso_menor}.')
