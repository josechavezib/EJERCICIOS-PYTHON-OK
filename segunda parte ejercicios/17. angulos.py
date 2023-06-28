angulo = int(input("ingresa el valor del angulo: "))

if angulo < 90:
    print("el angulo ingresado", str(angulo)+str("º"), "es agudo.")
elif angulo == 90:
    print("el angulo ingresado", str(angulo)+str("º"), "es recto.")
elif angulo > 90:
    print("el angulo ingresado", str(angulo)+str("º"), "es obtuso.")
else:
    print("ingrese un valor valido")    