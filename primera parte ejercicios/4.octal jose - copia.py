x = int(input("ingrese un numero: "))
y = 8
cadena = ""
while x >=1:
    #( x, "/", y, " = ", x%y )
    cadena = str(x%y) + (cadena)
    x = x // y   
print ("el numero ingresado en octal es: ", cadena)