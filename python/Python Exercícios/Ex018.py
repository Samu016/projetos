import math
ang = float(input('Digite um angulo qualquer: '))
cosseno = math.cos(math.radians(ang))
seno = math.sin(math.radians(ang))
tangente = math.tan(math.radians(ang))
print(f'O cosseno vale {cosseno:.2f}\nO seno vale {seno:.2f}\nA tangente vale {tangente:.2f}')