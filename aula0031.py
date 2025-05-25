"""
Flag (Bandeira) - Marcar um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

# v1 = 'a'
# v2 = 'a'
# print(id(v1))  # Como ambas as variáveis possuem valores iguais
# print(id(v2))  # Ambas apontarão para o mesmo local na memória

condicao = False
passou_no_if = None

if condicao:
  passou_no_if = True
  print('Faça algo')
else:
  print('Não faça algo')


print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)