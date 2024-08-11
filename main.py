# 1) Solicita ao usuário que digite seu nome

nome = input('Digite seu nome: ')

# 2) Solicita ao usuário que digite o valor do seu salário

# Converte a entrada para um número de ponto flutuante

salario = float(input('Digite seu salario: '))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante


bonus = float(input('Digite valor do bonus: '))

# 4) Calcule o valor do bônus final 

valor_bonus_final = (1000 + salario) * bonus

# 5) Imprima cálculo do KPI para o usuário

print(f'O valor do bonus final será de : {valor_bonus_final}')

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f'{nome} seu valor de bonus final será de {valor_bonus_final}')

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?