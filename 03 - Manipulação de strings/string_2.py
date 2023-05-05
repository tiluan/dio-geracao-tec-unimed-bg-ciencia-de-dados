nome = "Luan"
idade = 32
profissao = "Analista BI"
linguagem = "Python"
saldo = 12.34

# Cria um dicionário com o nome e a idade
dados = {"nome": "Luan", "idade": 323}

# Utiliza o operador % para inserir valores de variáveis em uma string com formatação.
print("Nome: %s Idade: %d" % (dados['nome'], dados['idade']))

# Utiliza o método format() para inserir valores de variáveis em uma string com formatação.
print("Nome: {} Idade: {}".format(dados['nome'], dados['idade']))

# Utiliza o método format() para inserir valores de variáveis em uma string com formatação, especificando as posições das variáveis.
print("Nome: {0} Idade: {1}".format(dados['nome'], dados['idade']))

# Utiliza o método format() para inserir valores de variáveis em uma string com formatação, repetindo uma variável.
print("Nome: {0} Idade: {1} Nome: {0} {0} {0} {0}".format(dados['nome'], dados['idade']))

# Utiliza o método format() para inserir valores de variáveis em uma string com formatação, utilizando chaves com nomes de variáveis.
print("Nome: {name} Idade: {age}".format(name=dados['nome'], age=dados['idade']))

# Utiliza o método format() para inserir valores de variáveis em uma string com formatação, utilizando um dicionário.
print("Nome: {nome} Idade: {idade}".format(**dados))

# Utiliza uma f-string para inserir valores de variáveis em uma string com formatação.
print(f"Nome: {dados['nome']} Idade: {dados['idade']}")

# Utiliza uma f-string para inserir valores de variáveis em uma string com formatação, especificando o número de casas decimais para um valor numérico.
print(f"Nome: {dados['nome']} Idade: {dados['idade']} Saldo: {saldo:.2f}")

# Utiliza uma f-string para inserir valores de variáveis em uma string com formatação, especificando o número total de caracteres para um valor numérico.
print(f"Nome: {dados['nome']} Idade: {dados['idade']} Saldo: {saldo:10.2f}")
