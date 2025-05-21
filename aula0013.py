nome = 'David Rodrigues'
altura = 1.70
peso = 71
# imc = ...  # Os três pontos representa Ellipsis, um valor que ainda será preenchido e o Python ignora.
imc = peso / (altura * altura)

# David Rodrigues tem 1.70 de altura,
# pesa 71 quilos e seu IMC é
# 24.57
print(f'{nome} tem {altura:.2f} e altura,\npesa {peso} quilos e seu IMC é\n{imc:.2f}')