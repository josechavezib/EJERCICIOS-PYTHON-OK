inicio = int(input("Ingrese el número de inicio de la secuencia: "))

while True:
    print(inicio)

    respuesta = input("¿Desea continuar? (s/n): ")
    if respuesta.lower() != "s":
        break

    inicio += 1

    