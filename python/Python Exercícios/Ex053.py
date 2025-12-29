import uteis
uteis.titulo('palíndromo')
frase = str(input('Digite uma frase: ')).replace(" ", "").upper()
invertida = frase[::-1]
if frase == invertida:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
