from math import hypot
cateto_a = float(input('Digite o cateto adjacente: '))
cateto_b = float(input('Digite o cateto oposto: '))

hipotenusa = hypot(cateto_a, cateto_b)
print(f'A hipotenusa é {hipotenusa:.2f}')