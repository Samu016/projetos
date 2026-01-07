import uteis
uteis.titulo('Fatorial')

fatorial = int(input('Digite um número: '))
c = fatorial
b=1
while c >= 1:
    print(f'{c} x ' if c>1 else f'{c} = ', end='')
    b *= c
    c -= 1
print(f'{b}')