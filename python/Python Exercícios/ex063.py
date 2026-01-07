import uteis
uteis.titulo('Fibonacci')
quantidade = int(input('Quantos termos da sequência de fibonacci: '))

a,b,c,d=0,1,1,0
while c < quantidade:
    if c == 1:
        print(f'{a} -> {b}',end=' ')
    else:
        print(f'-> {d}', end=' ')
    d=a+b
    a=b
    b=d
    c+=1
