
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_str = input('Digite um número inteiro: ')
try:
    numero_int = int(numero_str)
    numero_e_par = numero_int % 2 == 0
    if numero_e_par:
        print('O número é par.')
    else:
        print('O número é ímpar.')
except:
    print('O número informado não é inteiro.')
    
    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Digite a hora: ')
hora_float = float(hora)

if hora_float > 0 and hora_float < 12:
    print('Bom dia!')
elif hora_float >= 12 and hora_float < 18:
    print('Boa tarde!')
elif hora_float >= 18 and hora_float < 24:
    print('Boa noite!')
else:
    print('Horário inválido.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu nome: ')

if len(nome) <= 4:
    print('Seu nome é curto.')
elif len(nome) >=5 and len(nome) <= 6:
    print('Seu nome é normal')
elif len(nome) > 6:
    print('Seu nome é muito grande.')
else:
    print('Nome inválido.')