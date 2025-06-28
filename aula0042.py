frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

# print(frase.count('Python'))

i = 0
qtd_apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''
while i < len(frase):

    

    letra_atual = frase[i]
    quantas_vezes_letra_apareceu_atual = frase.count(letra_atual)

    if letra_atual == ' ':
        i+= 1
        continue

    if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu_atual:
        qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu_atual
        letra_que_apareceu_mais_vezes = letra_atual

    i+= 1


print(letra_que_apareceu_mais_vezes)
