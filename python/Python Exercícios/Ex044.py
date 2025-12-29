import uteis
uteis.titulo('PAGAMENTO')

preco = float(input('Informe o preço do produto: '))
pagamento = int(input("""Informe a forma de pagamento: 
À VISTA (Dinheiro/cheque: 10% de desconto)) [1]
À VISTA NO CARTÃO (5% de desconto)) [2])
2X NO CARTÃO (Preço normal) [3])
3X OU MAIS NO CARTÃO (20% juros) [4]
"""))

if pagamento == 1:
    print(f'O valor final será de R$ \033[31m{preco*0.9:.2f}')
elif pagamento == 2:
    print(f'O valor final será de R$ \033[31m{preco*0.95:.2f}')
elif pagamento == 3:
    print(f'O valor final será de R$ \033[31m{preco:.2f}')
elif pagamento == 4:
    print(f'O valor final será de R$ \033[31m{preco*1.2:.2f}')
else:
    uteis.notas()