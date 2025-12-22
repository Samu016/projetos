dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
preco = dias * 60 + km * 0.15
print(f'O aluguel será de R${preco:.2f}')