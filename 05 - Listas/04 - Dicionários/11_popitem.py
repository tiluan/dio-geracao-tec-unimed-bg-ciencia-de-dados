# Criação de um dicionário
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Remoção de um elemento aleatório
resultado = contatos.popitem()

# Exibição do resultado
print(resultado)

# Tentativa de remoção de um elemento aleatório de um dicionário vazio
# contatos.popitem()  # KeyError