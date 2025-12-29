from uteis import titulo
titulo('PARES 1 A 50')
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=', ')
print('FIM')