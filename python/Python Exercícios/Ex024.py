nome = input('Digite o nome da sua cidade: ').strip()
cidade = nome.lower().split()
if cidade[0] == 'santo':
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com Santo')