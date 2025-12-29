from uteis import titulo
titulo('SOMA ÍMPARES MÚLTIPLOS DE 3')
soma = 0
cont = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        print(c)
        cont +=1
        soma += c
print(f'\033[32mA soma total dos {cont} valores solicitados é {soma}')