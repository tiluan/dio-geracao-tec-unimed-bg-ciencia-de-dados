matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])  # Acessa a primeira linha da matriz: (1, "a", 2)
print(matriz[0][0])  # Acessa o primeiro elemento da primeira linha: 1
print(matriz[0][-1])  # Acessa o último elemento da primeira linha: 2
print(matriz[-1][-1])  # Acessa o último elemento da última linha: "c"