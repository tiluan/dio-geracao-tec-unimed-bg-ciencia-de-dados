while True:
    numero = int(input("Informe um numero: "))

    if numero == 10:
        break

    if numero % 2 == 0: # Só da print quando são números impares
        continue

    print(numero)