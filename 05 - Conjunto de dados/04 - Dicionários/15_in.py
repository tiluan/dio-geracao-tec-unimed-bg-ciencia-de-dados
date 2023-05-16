# Criação de um dicionário
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Verificação de existência de uma chave
resultado = "guilherme@gmail.com" in contatos

# Exibição do resultado
print(resultado)

# Verificação de existência de uma chave inexistente
resultado = "megui@gmail.com" in contatos

# Exibição do resultado
print(resultado)

# Verificação de existência de um elemento
resultado = "idade" in contatos["guilherme@gmail.com"]

# Exibição do resultado
print(resultado)

# Verificação de existência de um elemento
resultado = "telefone" in contatos["giovanna@gmail.com"]

# Exibição do resultado
print(resultado)