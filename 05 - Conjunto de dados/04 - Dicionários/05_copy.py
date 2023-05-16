# Criação de um dicionário
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Cópia do dicionário
copia = contatos.copy()

# Atualização do elemento da cópia
copia["guilherme@gmail.com"] = {"nome": "Gui"}

# Exibição do elemento original
print(contatos["guilherme@gmail.com"])

# Exibição do elemento da cópia
print(copia["guilherme@gmail.com"])