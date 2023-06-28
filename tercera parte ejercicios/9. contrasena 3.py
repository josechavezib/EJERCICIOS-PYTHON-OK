print ("solo tienes 5 intentos para introducir tu conttrasena")
contador = 1
import time
while contador <= 5:
    contraseña = input("Introduce la contraseña: ")
    if contraseña == "123jose":
        print("la contraseña es correcta")
        contador = 6
    else:
        print("La contraseña es incorrecta sigue intentando")
        if contador == 5:
            print("has sobrepasado el numero de intentos")
        time.sleep(contador)
        contador = contador + 1