"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'David'
preco = 1000.95897643
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)  # Os tipos tem que estar de acordo com os placeholders
# variavel = 'David, o preço total foi R$1000.95'
print(variavel)

print('O hexadecimal de %d é %X' % (10, 10))