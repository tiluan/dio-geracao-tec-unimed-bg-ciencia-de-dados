# Criação de um dicionário
contato = {"nome": "Guilherme", "telefone": "3333-2221"}

# Atualização de um elemento existente
contato.setdefault("nome", "Giovanna")

# Exibição do resultado
print(contato)

# Atualização de um elemento inexistente
contato.setdefault("idade", 28)

# Exibição do resultado
print(contato)