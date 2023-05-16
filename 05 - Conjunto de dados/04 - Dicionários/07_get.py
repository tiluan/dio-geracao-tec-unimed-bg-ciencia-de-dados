# Criação de um dicionário
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Tentativa de acesso a um elemento inexistente
# contatos["chave"]  # KeyError

# Acesso a um elemento inexistente
resultado = contatos.get("chave")

# Exibição do resultado
print(resultado)

# Acesso a um elemento inexistente
resultado = contatos.get("chave", {})

# Exibição do resultado
print(resultado)

# Acesso a um elemento existente
resultado = contatos.get("guilherme@gmail.com", {})

# Exibição do resultado
print(resultado)