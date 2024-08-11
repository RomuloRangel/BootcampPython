# 1) Solicita ao usuário que digite seu nome
try:
    nome = input('Digite seu nome: ')

    if len(nome) == 0:
        raise ValueError('O nome não pode ser vazio')
        exit()

    # Verifica se há digito nos Input de nome
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
        exit()
    else:
        print("Nome válido:", nome)
except ValueError as e:
    print(e)
    exit()
    



# 2) Solicita ao usuário que digite o valor do seu salário


try:
    
    salario = float(input('Digite seu salario: '))
    if salario <= 0:
        print('O valor não pode ser negativo ! ') 
except ValueError:
    print("Digite um valor válido")
    exit()


# 3) Solicita ao usuário que digite o valor do bônus recebido


try:
    bonus = float(input('Digite valor do bonus: '))
    if bonus < 0:
        print("O valor do bonus não pode ser negativo")
        exit()
except ValueError:
    print("Digite um valor válido")
    exit()


# 4) Calcule o valor do bônus final 

valor_bonus_final = (1000 + salario) * bonus

# 5) Imprima cálculo do KPI para o usuário

print(f'O valor do bonus final será de : {valor_bonus_final}')

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f'{nome}, seu salario é de {salario} e valor de bonus final será de {valor_bonus_final}')

