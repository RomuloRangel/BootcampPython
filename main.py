nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is not True:

    try:
        nome = input('Digite seu nome: ').strip()

        if len(nome) == 0:
            raise ValueError('O nome não pode ser vazio')
           

        # Verifica se há digito nos Input de nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
           
        else:
            nome_valido = True
            print("Nome válido:", nome)
    except ValueError as e:
        print(e)
    
  
    

# 2) Solicita ao usuário que digite o valor do seu salário

while salario_valido is not True:
    try:
        salario = input('Digite seu salario ').strip()
        salario_novo = float(salario)

        if salario_novo <= 0:
            print('Não é aceito valor nulo ou menor que zero' )
        
        else:
            salario_valido = True
            print('Salario valido')
    
    except ValueError as e:

        print(e)

while bonus_valido is not True:   
    try:
        bonus = input('Digite seu bonus ')
        bonus_novo = float(bonus)

        if bonus_novo <=0:
            print('Não é aceito valor nulo ou menor que zero ')
        else:
            bonus_valido = True
            print("Bonus valido")
    except ValueError as e :
        print(e)


bonus_recebido = 1000 + salario_novo * bonus_novo  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${salario_novo:.2f} e seu bônus final é R${bonus_recebido:.2f}.")