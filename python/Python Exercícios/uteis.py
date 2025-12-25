def titulo(txt, esp):
    print('\033[33m=+\033[m' * 20)
    print(f'{' ' * esp}\033[32m{txt}\033[m')
    print('\033[33m=+\033[m' * 20)

def notas():
    print('\033[31mERROR! OPÇÃO INVÁLIDA\033[m')