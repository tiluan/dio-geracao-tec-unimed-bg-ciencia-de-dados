# Criação de um dicionário
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Remoção de um elemento
resultado = contatos.pop("guilherme@gmail.com")

# Exibição do resultado
print(resultado)

# Remoção de um elemento inexistente
resultado = contatos.pop("guilherme@gmail.com", {})

# Exibição do resultado
print(resultado)