# Criação de um dicionário
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Iteração sobre as chaves
for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

# Iteração sobre os itens
for chave, valor in contatos.items():
    print(chave, valor)