# Define o conjunto de carros
carros = {"gol", "celta", "palio"}

# Imprime cada carro no conjunto
for carro in carros:
    print(carro)

# Imprime o índice e o elemento correspondente
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
