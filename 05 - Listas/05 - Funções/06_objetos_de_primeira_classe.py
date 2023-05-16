# Definição de função
def somar(a, b): # Define uma função com dois parâmetros obrigatórios
    return a + b # Retorna a soma dos parâmetros

def exibir_resultado(a, b, funcao): # Define uma função com três parâmetros obrigatórios
    resultado = funcao(a, b) # Chama a função passada como parâmetro
    print(f"O resultado da operação {a} + {b} = {resultado}") # Imprime o resultado da operação

# Chamada de função
exibir_resultado(10, 10, somar) # Chama a função com três parâmetros obrigatórios, sendo o último a função somar
# Saída: O resultado da operação 10 + 10 = 20