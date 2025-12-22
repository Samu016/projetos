num = input('Digite um número de 0 a 9999: ')
algarismo = [int(x) for x in num if x.isdigit()][::-1]
casas = ['Unidade', 'Dezena', 'Centena', 'Milhar']

for i in range(len(algarismo)):
    print(f'{casas[i]} - {algarismo[i]}')

"""
if len(algarismo) == 4:
    print(f'''
    Unidade: {algarismo[-1]}
    Dezena: {algarismo[-2]}
    Centena: {algarismo[-3]}
    Milhar: {algarismo[-4]}''')
elif len(algarismo) == 3:
    print(f'''
    Unidade: {algarismo[-1]}
    Dezena: {algarismo[-2]}
    Centena: {algarismo[-3]}''')
elif len(algarismo) == 2:
    print(f'''
    Unidade: {algarismo[-1]}
    Dezena: {algarismo[-2]}
    ''')
else:
    print(f'Unidade: {algarismo[0]}')
"""