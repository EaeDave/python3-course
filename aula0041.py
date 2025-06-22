# while/else

string = 'Valor qualquer'

i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break  # Se o while encontrar break, então o else não é executado.
    # Caso o while termine o laço sem erros ou break, o else é executado junto.

    print(letra)
    i += 1
else:
    print('O else foi execuado.')