salario = int(input('Informe seu salario: '))
if salario >= 1250:
    print(f'Seu novo salário é {salario*1.10:.2f} reais!')
else:
    print(f'Seu novo salário é {salario*1.15:.2f} reais!')