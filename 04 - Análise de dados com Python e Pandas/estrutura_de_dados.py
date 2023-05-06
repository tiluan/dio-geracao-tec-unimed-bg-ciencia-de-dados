"""# **Listas**"""

# Criando uma lista chamada animais com os elementos 1, 2 e 3
animais = [1, 2, 3]
print(animais)

# Criando uma lista chamada animais com os elementos "cachorro", "gato", 12345 e 6.5
animais = ["cachorro", "gato", 12345, 6.5]
print(animais)

# Imprimindo o primeiro elemento da lista
print(animais[0])

# Imprimindo o 4 elemento da lista
print(animais[3])

# Substituindo o primeiro elemento da lista por "papagaio"
animais[0] = "papagaio"
print(animais)

# Removendo "gato" da lista
animais.remove("gato")
print(animais)

# Obtendo o tamanho da lista "animais"
print(len(animais))

# Verificando se "gato" está na lista "animais"
print("gato" in animais)

# Criando uma lista chamada lista com os elementos 500, 30, 300, 80 e 10
lista = [500, 30, 300, 80, 10]

# Obtendo o maior valor da lista "lista"
print(max(lista))

# Obtendo o menor valor da lista "lista"
print(min(lista))

# Adicionando a lista ["leão", "Cachorro"] como um elemento da lista "animais"
animais.append(["leão", "Cachorro"])
print(animais)

# Adicionando os elementos "cobra" e 6 à lista "animais"
animais.extend(["cobra", 6])
print(animais)

# Contando quantas vezes o elemento "leão" aparece na lista "animais"
print(animais.count("leão"))

# Ordenando a lista "lista" em ordem crescente
lista.sort()
print(lista)


"""# **Tuplas**"""

#As tuplas usam parênteses como sintaxe

# Definindo uma tupla chamada tp com os elementos "Banana", "Maçã", 10 e 50
tp = ("Banana", "Maçã", 10, 50)

print(tp[0]) # Acessando o primeiro elemento da tupla, que é "Banana"

# Tentando atribuir "Laranja" ao primeiro elemento da tupla, o que não é possível, pois tuplas são imutáveis
# tp[0] = "Laranja"

print(tp.count("Maçã")) # Contando quantas vezes o elemento "Maçã" aparece na tupla

print(tp[0:2]) # Imprimindo os dois primeiros elementos da tupla, ou seja, "Banana" e "Maçã"


"""# **Dicionários**"""

#Para criar um dicionário utilizamos as {}
# Criação de um dicionário com as quantidades de frutas
dc = {"Maçã":20, "Banana":10, "Laranja":15, "Uva":5}

# Exibe o dicionário na tela
print(dc)

# Acessa o valor da chave "Maçã" no dicionário e o exibe na tela
print(dc["Maçã"])

# Altera o valor da chave "Maçã" no dicionário
dc["Maçã"] = 25

# Exibe o dicionário atual

print(dc)

# Retorna todas as chaves do dicionário e as exibe na tela
print(dc.keys())

# Retorna todos os valores do dicionário e os exibe na tela
print(dc.values())

# Define o valor padrão da chave "Limão" no dicionário, caso ela não exista
dc.setdefault("Limão", 22)

# Exibe o dicionário atualizado na tela
print(dc)
