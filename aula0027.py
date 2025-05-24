"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[4:])  # Ao especificar o início e deixar o fim em branco com ":", o fatiamento irá até o final da str
print(variavel[4:9])  # O índice final do fatiamente geralmente é excluído, por isso foi até 9
print(len(variavel))  # Retorna a qtd de caracteres - 9
print(variavel[0:9:2])  # O [i:f:"2"] é a qtd de passos que será retornado, de quantos em quantos caracteres
print(variavel[::-1])  # Invertendo uma str