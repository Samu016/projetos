import uteis
uteis.titulo('progressão aritimética')

t1 = int(input('primeiro termo: '))
r = int(input('razão: '))
qtd = int(input('quantidade de termos: '))
c = 0
while c < qtd:
    print(f'\033[32m{t1} -> \033[m', end='')
    t1 += r
    c += 1
print('FIM')
