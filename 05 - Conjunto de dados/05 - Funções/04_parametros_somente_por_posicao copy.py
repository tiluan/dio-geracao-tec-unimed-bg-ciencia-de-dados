# Definição de função

# Define uma função com seis parâmetros, sendo três obrigatórios e três opcionais
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): 
    print(modelo, ano, placa, marca, motor, combustivel) # Imprime os parâmetros

# Chamada de função

# Chama a função com três parâmetros obrigatórios e três parâmetros opcionais
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") 

# Inválido - a chamada de função deve conter um parâmetro obrigatório e três parâmetros opcionais
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") 