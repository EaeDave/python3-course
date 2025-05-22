# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

nome = 'Davi'

print('D' in nome)  # True

if 'David' in nome:
    print('Seu nome é David.')
else:
    print('Seu nome não é David.')  # True

frase = 'O rato roeu a roupa do rei de roma'

print('Amigo' not in frase)  # True