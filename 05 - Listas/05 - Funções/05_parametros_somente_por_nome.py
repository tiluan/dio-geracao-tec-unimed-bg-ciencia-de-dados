# Definição de função
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel): # Define uma função com sete parâmetros, sendo três obrigatórios, um opcional e três nomeados
    print(modelo, ano, placa, marca, motor, combustivel) # Imprime os parâmetros

# Chamada de função

 # Chama a função com três parâmetros obrigatórios, um opcional e três parâmetros nomeados
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

# Inválido - a chamada de função deve conter um parâmetro obrigatório, um opcional e três parâmetros nomeados
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") 