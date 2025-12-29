import uteis
uteis.titulo('Nomes e idades')
maior = 0
menos_20 = 0
soma = 0
for c in range(1, 5):
    print(f'{'-'*5}{c}° PESSOA{'-'*5}')
    nome = str(input('Digite o seu nome: '))
    sexo = str(input('Digite o seu sexo: [M/F]')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        uteis.notas()
        break
    idade = int(input('Digite sua idade: '))
    if sexo == 'M' and idade > maior:
        maior = idade
        homem_mais_velho = nome
    if sexo == 'F' and idade < 20:
        menos_20 += 1
    soma+=idade
print(f"""\033[1;32mA média de idade do grupo é de {soma/4:.2f} anos.
O homem mais velho é o {homem_mais_velho} e tem {maior} anos.
Existem {menos_20} mulheres com menos de 20 anos.
""")
