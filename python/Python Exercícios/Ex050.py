from uteis import titulo
titulo('SOMA PARES')
soma = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}° numero: '))
    if n % 2 == 0:
        soma += n
print(f'\033[31mA soma total é {soma}\033[m')