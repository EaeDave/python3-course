"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Digite um número: ')

try:
    numero_float = float(numero_str)  # Tentando converter para float
    print(f'O dobro de {numero_float} é = {numero_float * 2:.2f}')
except:  # Se acontecer esse erro, então faça o código abaixo:
    print('Digite somente números.')