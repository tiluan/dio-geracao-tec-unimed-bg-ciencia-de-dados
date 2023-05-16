# Definição de variável
salario = 2000 # Define a variável salário com o valor 2000

# Definição de função
def salario_bonus(bonus): # Define uma função com um parâmetro obrigatório
    global salario # Declara a variável salário como global
    salario += bonus # Adiciona o bonus ao salário
    return salario # Retorna o novo valor do salário

# Chamada de função
salario_bonus(500) # Chama a função com o parâmetro bonus com o valor 500
# Saída: 2500