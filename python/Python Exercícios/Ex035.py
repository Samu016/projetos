a = int(input('Digite a primeira reta: '))
b = int(input('Digite a segunda reta: '))
c = int(input('Digite a terceira reta: '))

if a+b>c and a+c>b and b+c>a:
    print('As três retas formam um triângulo!')
else:
    print('As três retas não formam um triãngulo!')