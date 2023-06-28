n1 = int(input("ingrasa el numero de inicio: "))
n2 = int(input("ingrasa el numero final: "))

print("los numero impares del rango,", n1, "al", n2, "son: ")
for i in range (n1,n2+1):
    if i % 2 != 0:
        print(i, end=",")