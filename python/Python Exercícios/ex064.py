import uteis
uteis.titulo('Números Aleatórios')

n1 = int(input('Digite o 1° número: '))
a,c=0,1
while n1 != 999:
    c+=1
    a+=n1
    n1 = int(input(f'Digite o {c}° número: '))
print(f'''
Foram digitados \033[32m{c-1}\033[m números.
A soma total é \033[34m{a}\033[m.
''')