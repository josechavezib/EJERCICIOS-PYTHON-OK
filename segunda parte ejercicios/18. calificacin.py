cal = int(input("ingrasa el numero de la calificacion: "))

if cal >= 90 and cal <= 100:
    print(" su calificacion es: A")
elif cal < 90 and cal >= 80:
    print(" su calificacion es: B")
elif cal < 80 and cal >= 70:
    print(" su calificacion es: C")
elif cal < 70 and cal >= 69:
    print(" su calificacion es: D")
elif cal < 69:
    print(" su calificacion es: F")
else:
    print("ingrese una calificacion valida")
    