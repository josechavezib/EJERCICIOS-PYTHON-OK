a = input("ingresa un numero: ")   
b = input("ingresa un numero: ")
c = input("ingresa un numero: ")
#a=2
#b=1
#c=3
if a != b and a != c and b != c:
    if a>b and a<c or a<b and a>c:
        print("el numero central es:", a)
    elif b>a and b<c or b<a and b>c:
        print("el numero central es:", b)
    elif c>a and c<b or c<a and c>b:
        print("el numero central es:", c)
else:
    print("los valores deben ser diferentes.")


