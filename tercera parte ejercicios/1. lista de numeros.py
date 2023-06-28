n1 = int(input("ingrasa el numero de inicio: "))
n2 = int(input("ingrasa el numero final: "))

if n2 > 0:
    for i in range (n1,n2+1):
    #print(i)
        print(i, end=",")
elif n2 < 0:
    for i in range (n1,n2-1,-1):
        #print(i)
        print(i, end=",")
        
        
