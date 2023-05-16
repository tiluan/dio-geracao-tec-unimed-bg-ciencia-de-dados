lista = ["p", "y", "t", "h", "o", "n"]

# Imprime os elementos da lista a partir do índice 2 até o final
print(lista[2:])  # ["t", "h", "o", "n"]

# Imprime os elementos da lista do início até o índice 1 (exclusivo)
print(lista[:2])  # ["p", "y"]

# Imprime os elementos da lista a partir do índice 1 até o índice 2 (exclusivo)
print(lista[1:3])  # ["y", "t"]

# Imprime os elementos da lista do início até o índice 3 (exclusivo) pulando de 2 em 2
print(lista[0:3:2])  # ["p", "t"]

# Imprime todos os elementos da lista
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]

# Imprime todos os elementos da lista em ordem reversa
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]