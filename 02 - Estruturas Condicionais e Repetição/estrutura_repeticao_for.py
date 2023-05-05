texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # Adiciona uma quebra de linha
    print("Executa no final do laço")


# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5): # Começando em 0, terminando em 50 (51 não é inclusivo), iterador de 5 em 5a
    print(numero, end="")