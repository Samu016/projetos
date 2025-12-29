from uteis import titulo
titulo('progressão aritmética')
t1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
decimo = t1 + (10 - 1) * razao
contador = 0
print(decimo)
for c in range(t1, decimo+1, razao):
    print(f'{contador}° Termo: {c}')
