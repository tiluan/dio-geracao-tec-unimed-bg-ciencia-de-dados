carros = ["gol", "celta", "palio"]

# Iterando sobre a lista de carros e imprimindo cada elemento
for carro in carros:
    print(carro)

# Iterando sobre a lista de carros e imprimindo o índice e o elemento usando a função enumerate()
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")