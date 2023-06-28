nombre= input("ingrese su nombre completo: ")
cont=1

for i in nombre:
    if i in "abcdefghijklmnñopqrstuvxyz":
        cont = cont +1
print("tu nombre tiene " + str(cont) + " caracteres")











#print (len(nombre))
