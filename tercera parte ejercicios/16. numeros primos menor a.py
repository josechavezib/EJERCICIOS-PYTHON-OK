n = int(input("ingrese un numero: "))

#if n > 0:
for i in range(2, n):
    contador=2
    esprimo = True
    while esprimo and contador <i:
        if i % contador == 0:
            espimo = False
        else:
            contador+=1
    if esprimo:
        print(i, "es primo")   
#else:
    #print(" ingresa un valor valido")     