# Lista de linguagens
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordenação em ordem crescente
linguagens.sort()
print(linguagens)

# Ordenação em ordem decrescente
linguagens.sort(reverse=True)
print(linguagens)

# Ordenação pelo tamanho da string em ordem crescente
linguagens.sort(key=lambda x: len(x))
print(linguagens)

# Ordenação pelo tamanho da string em ordem decrescente
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)