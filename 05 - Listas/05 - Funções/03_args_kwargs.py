# Definição de função
def exibir_poema(data_extenso, *args, **kwargs): # Define uma função com um parâmetro obrigatório e parâmetros opcionais
    texto = "\n".join(args) # Junta os parâmetros opcionais em uma única string
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]) # Junta os parâmetros nomeados em uma única string
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}" # Cria uma mensagem formatada
    print(mensagem) # Imprime a mensagem

# Chamada de função
exibir_poema(
    "Zen of Python", # Primeiro parâmetro obrigatório
    "Beautiful is better than ugly.", # Parâmetros opcionais
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters", # Parâmetros nomeados
    ano=1999,
)