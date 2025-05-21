# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print(1 + 1)  # int + int = soma
print('a' + 'b')  # str + str = concatenação

print(int('1'), type(int('1')))
print(int('1') + 1)
# print(int('str'))  # Retorna um erro pois não é possível converter uma cadeia de caracteres em um número, não estando na base 10.
print(bool(' '))  # Um espaço vazio já pode ser considerado true.