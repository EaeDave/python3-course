"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador < 10:
    contador+= 1

    if contador == 5:
        print('Não foi exibido o 5.')
        continue  # Retorna no início do laço

    print(contador)


print('Acabou')