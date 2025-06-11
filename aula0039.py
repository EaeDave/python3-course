"""
Iterando stirngs com while
"""

nome = 'David Rodrigues'  # Iteráveis
contador = 0
qtd_caracteres = len(nome)
nova_string = '*'

while contador < qtd_caracteres:
    letra = nome[contador]
    print(letra)
    nova_string += letra + '*'
    contador += 1


print(nova_string)