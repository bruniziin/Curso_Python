# Operadores in e not in
# Strigs são iteráveis
#  0 1 2 3 4 5
#  B r u n i s
# -6-5-4-3-2-1

# nome = 'Brunis'
# # print(nome[2])
# # print(nome[-4])
# print('u' in nome)
# print('z' in nome)
# print(10 * '-')
# print('nis' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que você quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
