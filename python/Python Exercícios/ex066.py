import uteis
uteis.titulo('Números Aleatórios')

a,c=0,0
while True:
    n1 = int(input(f'Digite o {c+1}° número: '))
    if n1 == 999:
        break
    c+=1
    a+=n1
print(f'''
Foram digitados \033[32m{c}\033[m números.
A soma total é \033[34m{a}\033[m.
''')
