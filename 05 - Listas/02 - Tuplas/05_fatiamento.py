# Definindo a tupla
tupla = ("p", "y", "t", "h", "o", "n",)

# Imprimindo os elementos da tupla a partir do índice 2 até o final
print(tupla[2:])  # Resultado: ("t", "h", "o", "n")

# Imprimindo os elementos da tupla do início até o índice 2 (exclusivo)
print(tupla[:2])  # Resultado: ("p", "y")

# Imprimindo os elementos da tupla do índice 1 até o índice 3 (exclusivo)
print(tupla[1:3])  # Resultado: ("y", "t")

# Imprimindo os elementos da tupla do índice 0 até o índice 3 (exclusivo) com passo 2
print(tupla[0:3:2])  # Resultado: ("p", "t")

# Imprimindo todos os elementos da tupla
print(tupla[::])  # Resultado: ("p", "y", "t", "h", "o", "n")

# Imprimindo todos os elementos da tupla em ordem inversa
print(tupla[::-1])  # Resultado: ("n", "o", "h", "t", "y", "p")