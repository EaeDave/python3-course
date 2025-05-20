# \r\n -> CRLF (Normalmente Windows)
# \n -> LF (Normalmente Unix)

print('Oi, eu sou o David!')  # print() é uma função que exibe na tela o que recebe como argumento.
print(12, 34, sep='\n', end='##\n')  # Também é possível receber múltiplos argumentos.
print(56, 78, sep='?')  # É possível utilizar argumentos em parâmetros nomeados
# para alterar o comportamento padrão da função.

# O separador do 2° print foi uma quebra de linha utilizando \n,
# já o 3°, utilizou uma enterrogação.