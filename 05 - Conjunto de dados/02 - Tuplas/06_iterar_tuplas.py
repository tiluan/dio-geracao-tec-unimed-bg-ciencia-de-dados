carros = (
    "gol",
    "celta",
    "palio",
)

# Iterando sobre a tupla de carros e exibindo cada um deles
for carro in carros:
    print(carro)

# Iterando sobre a tupla de carros e exibindo o índice e o valor de cada um
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")