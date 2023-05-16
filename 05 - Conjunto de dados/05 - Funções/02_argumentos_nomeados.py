# Definição de função

# Define uma função com quatro parâmetros
def salvar_carro(marca, modelo, ano, placa): 
    # Imprime uma mensagem formatada com os parâmetros
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}") 

# Chamada de função
# Chama a função com quatro parâmetros
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# Chama a função com quatro parâmetros usando nomeação
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") 

# Chama a função com quatro parâmetros usando desempacotamento de dicionário
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) 