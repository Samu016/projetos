#Enfeite
print("\033[1;33m=\033[m" * 30)
print("\033[1;33m EMPRÉSTIMO BANCÁRIO\033[m")
print("\033[1;33m=\033[m" * 30)
#Campo de entrada do Usuário
nome = str(input("\033[32m Digite o seu nome: \033[m"))
casa = float(input("\033[32m Digite o valor da casa: \033[m"))
salario = float(input('\033[32m Digite seu salário: \033[m'))
anos = int(input('\033[32m Em quantos anos deseja pagar: \033[m'))
#Definindo o pagamento do usuário (prestações e em quantos meses pagará)
meses = anos * 12
prestacao = casa / meses
pagamento = salario * 0.3

print(f'A prestação ficou por \033[31mR$ {prestacao:.2f}\033[m.')
if prestacao > pagamento:
    print('O valor das parcelas excedeu os 30% do seu salário.\nPor favor, aumente os anos.')
else:
    print(f'Parabéns, \033[3;33m{nome}\033[m! A casa é sua.')
