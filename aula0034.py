"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""

# while True:
#     print('Loop infinito.')

while True:
    deseja_sair = input('Deseja sair? [S]im ou [N]ão? ')
    deseja_sair_lower = deseja_sair.lower()

    deseja_sair_true = deseja_sair_lower == 's' or deseja_sair_lower == 'sim'
    deseja_sair_false = deseja_sair_lower == 'n' or deseja_sair_lower == 'nao' or deseja_sair_lower == 'não'
    
    if deseja_sair_true:
        print('Sistema encerrado.')
        break  # Quebra o laço de repetição
    elif deseja_sair_false:
        print('Sistema não encerrado, retornando a pergunta...')
    else:
        print('Opção incorreta.')


print('Essa mensagem só foi exibida quando o laço terminou.')