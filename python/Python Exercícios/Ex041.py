import uteis
from datetime import date
uteis.titulo('CLASSIFICAÇÃO DE CATEGORIA')

ano = int(input('\033[33mQual o ano do seu nascimento? \033[m'))
hoje = date.today().year
categoria = hoje - ano

print(f'Você tem \033[33m{categoria}\033[m anos.')
if categoria <= 9:
    print('\033[32mMIRIN\033[m')
elif 9 < categoria <= 14:
    print('\033[32mINFANTIL\033[m')
elif 14 < categoria <= 19:
    print('\033[32mJUNIOR\033[m')
elif 19 < categoria <= 20:
    print('\033[32mSÊNIOR\033[m')
else:
    print('\033[32mMASTER\033[m')