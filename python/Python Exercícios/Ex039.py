from datetime import date

print('\033[33m=+\033[m'*20)
print(f'{' '*10}\033[32mALISTAMENTO MILITAR\033[m')
print('\033[33m=+\033[m'*20)

ano = int(input('Em que ano você nasceu? '))

idade = date.today().year - ano
if idade < 18:
    print(f'Você é menor que 18 anos! Ainda faltam {18 - idade} anos para o alistamento!\nVocê irá se alistar em {date.today().year + 18 - idade} anos para o alistamento!')
elif idade == 18:
    print('\033[1;33mVocê tem 18 anos! Você já deve se alistar')
else:
    print(f'\033[1;31mVocê tem mais que 18 anos! Você já deveria ter se alistado a {idade-18} anos!\nVocê deveria ter se alistado a {date.today().year - (idade-18)} anos!')
