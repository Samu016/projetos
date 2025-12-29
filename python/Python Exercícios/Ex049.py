from uteis import titulo
titulo('TABUADA')
n1 = int(input('Digite um numero: '))
for c in range(1, 11):
    print(f'| {n1} x {c} = {n1 * c} |')
print(f'\033[32mFIM\033[m')