# Calculadora com while

operadores_validos = ['+', '-', '*', '/']


continuar_laco = True

while continuar_laco:
    operador = input('Qual operação você deseja fazer? Somar[+], Subrair[-], Multiplicar[*]ou Dividir[/]:')
    if operador not in operadores_validos:
        print('Operador inválido, envie somente o símbolo do operador que deseja.')
        continue

    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')

    if num_1.isdigit() and num_2.isdigit():
        num1_float = float(num_1)
        num2_float = float(num_2)

        if operador == '+':
            soma = num1_float + num2_float
            print(soma)
        elif operador == '-':
            subtracao = num1_float - num2_float
            print(subtracao)
        elif operador == '*':
            multiplicacao = num1_float * num2_float
            print(multiplicacao)
        elif operador == '/':
            divisao = num1_float / num2_float
            print(divisao)


        while continuar_laco:
            deseja_continuar = input('Deseja realizar outra operação? [S]im ou [N]ão: ').lower()
            continuar = ['sim', 's']
            sair = ['n', 'nao', 'não']

            if deseja_continuar in continuar:
                break
            elif deseja_continuar in sair:
                print('Calculadora encerrada com sucesso!')
                continuar_laco = False
            else:
                print('Opção inválida.')
                continue
