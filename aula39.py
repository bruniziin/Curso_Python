"""
Iterando strings com while
"""
#       012345678910
nome = 'Bruno Felipe' # Iteráveis
#      121110987654321
# tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome
# print(nome[4])
# nova_string += '*B*r*u*n*o *F*e*l*i*p*e'

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)




