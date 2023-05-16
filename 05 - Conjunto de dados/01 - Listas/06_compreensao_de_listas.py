# Lista de números
numeros = [1, 30, 21, 2, 9, 65, 34]

# Filtrando os números pares utilizando list comprehension
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Calculando o quadrado de cada número utilizando list comprehension
quadrado = [numero**2 for numero in numeros]
print(quadrado)