nome = str(input('Digite seu nome completo: ')).strip()
print(f'Em letras maiusculas: {nome.upper()}')
print(f'Em letras minusculas: {nome.lower()}')
"""
contador = 0
for letra in nome:
    if letra.isalpha():
        contador += 1
print(f'Quantidade de letras: {contador}')
"""
letras = [letter for letter in nome if letter.isalpha()]
print(f'Quantidade de letras: {len(letras)}')

primeiro_nome = nome.split()
print(f'Primeiro nome: {primeiro_nome[0]} e tem {len(primeiro_nome[0])} letras')
