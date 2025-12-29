from datetime import date
import uteis
uteis.titulo('maioridade')
ano_atual = date.today().year
contM = 0
contm = 0
for c in range(1, 8):
    ano = int(input(f'Ano de nascimento da {c}° pessoa: '))
    idade = ano_atual - ano
    if idade >= 18:
        contM += 1
    else:
        contm += 1

print(f"""Há {contM} pessoas com mais de 18 anos.
Há {contm} pessoas com menos de 18 anos.""")