nome = input('Digite o seu nome: ')

print(f'Muito prazer, {nome}. Seja bem-vindo!')

numero_1 = float(input('Digite um número: '))  # É preciso fazer o typecasting para float ou int, pois a função input()
# retorna str por padrão, e soma entre str é = concatenação
numero_2 = float(input('Digite outro número: '))

print(f'A soma entre {numero_1:.2f} e {numero_2:.2f} é = {(numero_1 + numero_2):.2f}')
