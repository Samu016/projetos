import uteis
from sympy import isprime
uteis.titulo('números primos')
for c in range(0,11):
    n = int(input('Digite um número: '))
    if isprime(n) == True:
        print('PRIMO')
    else:
        print('NÃO PRIMO')
    resposta = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resposta == 'S':
        continue
    elif resposta == 'N':
        break
    else:
        uteis.notas()
        break
print('FIM DO PROGRAMA')