# Criação de um dicionário
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Remoção de um elemento
del contatos["guilherme@gmail.com"]["telefone"]

# Remoção de um elemento
del contatos["chappie@gmail.com"]

# Exibição do resultado
print(contatos)