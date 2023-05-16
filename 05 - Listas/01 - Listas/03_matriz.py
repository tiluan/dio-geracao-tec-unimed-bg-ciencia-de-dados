# Uma matriz é uma estrutura de dados retangular composta por elementos organizados em linhas e colunas. 
# Em Python, uma matriz é comumente representada como uma lista de listas, onde cada lista interna representa uma linha da matriz.

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # Imprime a primeira linha da matriz: [1, "a", 2]
print(matriz[0][0])  # Imprime o primeiro elemento da primeira linha: 1
print(matriz[0][-1])  # Imprime o último elemento da primeira linha: 2
print(matriz[-1][-1])  # Imprime o último elemento da última linha: "c"
