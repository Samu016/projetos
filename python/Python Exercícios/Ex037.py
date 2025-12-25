print('\033[33m=\033[m'*30)
print('\033[33mCONVERSÃO DE BASES\033[m')
print('\033[33m=\033[m'*30)

n1 = int(input('Digite um número inteiro: '))
opcao = int(input("""
Digite para qual base numérica deseja converter:
Binário = 1
Octal = 2
Hexadecimal = 3
"""))

if opcao == 1:
    print(f'O número \033[31m{n1}\033[m em binário é \033[32m{bin(n1)[2:]}')
elif opcao == 2:
    print(f'O número \033[31m{n1}\033[m em octal é \033[32m{oct(n1)[2:]}')
elif opcao == 3:
    print(f'O número \033[31m{n1}\033[m em hexadecimal é \033[32m{hex(n1)[2:]}')
else:
    print('\033[31mERROR! Opção inválida!')
