nome = "LuaN"

# Imprime a string nome em letras maiúsculas.
print(nome.upper())

# Imprime a string nome em letras minúsculas.
print(nome.lower())

# Imprime a string nome com a primeira letra de cada palavra em maiúscula e as demais em minúsculas.
print(nome.title())

texto = "     Olá, mundo!       "

# Imprime a variável texto concatenada com um ponto final.
print(texto + ".")

# Imprime a variável texto sem os espaços em branco no início e no final, concatenada com um ponto final.
print(texto.strip() + ".")

# Imprime a variável texto sem os espaços em branco no final, concatenada com um ponto final.
print(texto.rstrip() + ".")

# Imprime a variável texto sem os espaços em branco no início, concatenada com um ponto final.
print(texto.lstrip() + ".")

menu = "Python"

# Imprime a string menu centralizada em uma largura de 14 caracteres, com espaços em branco ao redor.
print(menu.center(14))

# Imprime a string menu centralizada em uma largura de 14 caracteres, com caracteres "#" ao redor.
print(menu.center(14, "#"))

# Imprime os caracteres da string menu separados pelo caractere "-".
print("-".join(menu))