print('\033[33m=+\033[m'*20)
print(f'{' '*12}\033[32mMÉDIA DO ALUNO\033[m')
print('\033[33m=+\033[m'*20)
nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2
print(f'Com {nota1} e {nota2} sua média foi {media:.2f}')
if media >= 7:
    print('\033[34mAPROVADO!\033[m')
elif media < 5:
    print('\033[31mREPROVADO!\033[m')
else:
    print('\033[33mRECUPERAÇÃO!\033[m')