# Criação de um dicionário
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Atualização de um elemento existente
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})

# Exibição do resultado
print(contatos)

# Atualização de um elemento inexistente
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})

# Exibição do resultado
print(contatos)