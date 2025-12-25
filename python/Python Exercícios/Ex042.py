a = int(input('Digite a primeira reta: '))
b = int(input('Digite a segunda reta: '))
c = int(input('Digite a terceira reta: '))

if a+b>c and a+c>b and b+c>a:
    print('As três retas formam um triângulo!')
    if a==b==c:
        print('É um triângulo equilátero!')
    elif a!=b!=c:
        print('É um triângulo escaleno!')
    else:
        print('É um triângulo isósceles!')
else:
    print('As três retas não formam um triãngulo!')