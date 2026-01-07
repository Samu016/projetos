import uteis
uteis.titulo('Tabuada')

while True:
    uteis.linha()
    n1 = int(input('Digite um número: '))
    if n1 <= 0:
        break
    uteis.linha()
    for c in range(1, 11):
        print(f'{n1} x {c} = {n1 * c}')
    uteis.linha()
print('FIM DO PROGRAMA')
