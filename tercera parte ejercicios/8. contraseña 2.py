print ("solo tienes 3 intentos para introducir tu conttrasena")
contador = 1
while contador <= 3:
    contraseña = input("Introduce la contraseña: ")
    if contraseña == "123jose":
        print("la contraseña es correcta")
        contador = 4
    else:
        print("La contraseña es incorrecta sigue intentando")
        if contador == 3:
            print("has sobrepasado el numero de intentos")
        contador = contador + 1