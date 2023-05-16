# Criação de dois conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# Verificação se o conjunto_a é um superconjunto de conjunto_b
resultado = conjunto_a.issuperset(conjunto_b)

# Exibição do resultado
print(resultado)

# Verificação se o conjunto_b é um superconjunto de conjunto_a
resultado = conjunto_b.issuperset(conjunto_a)

# Exibição do resultado
print(resultado)