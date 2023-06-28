frase= input("escribe una frase: ")
vocales= ["a", "e", "i", "o", "u"]

for i in vocales:
    contador= 0
    for x in frase:
        if x == i:
            contador= contador + 1
    print("La vocal ", i, " aparece ",contador, " veces")     