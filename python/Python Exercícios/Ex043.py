print('\033[33m=+\033[m'*20)
print(f'{' '*18}\033[32mIMC\033[m')
print('\033[33m=+\033[m'*20)

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('\033[1;31mABAIXO DO PESO\033[m')
elif imc < 25:
    print('\033[1;31mPESO NORMAL\033[m')
elif imc < 30:
    print('\033[1;31mACIMA DO PESO\033[m')
elif imc < 40:
    print('\033[1;31mSOBREPESO\033[m')
else:
    print('\033[1;31mOBESIDADE MÓRBIDA\033[m')
