# Definindo a lista de linguagens
linguagens = ["python", "js", "c", "java", "csharp"]

# Ordenando a lista de linguagens por comprimento em ordem crescente
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]

# Ordenando a lista de linguagens por comprimento em ordem decrescente
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]