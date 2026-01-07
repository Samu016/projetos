def titulo(txt):
    cont = len(txt)
    esp = int((40-cont)//2)
    print('\033[33m=+\033[m' * 20)
    print(f'{' ' * esp}\033[34m{txt.upper()}\033[m')
    print('\033[33m=+\033[m' * 20)

def notas():
    print('\033[31mERROR! OPÇÃO INVÁLIDA!\033[m')

def linha():
    print('\033[34m-\033[m' * 35)