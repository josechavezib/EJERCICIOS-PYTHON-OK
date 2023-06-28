
import random
intentosRealizados =0

número = random.randint(1, 20)
print("estoy pensando en un número entre 1 y 20.")

while intentosRealizados < 7:
    print('Intenta adivinar.')
    adivinar = int(input())
    intentosRealizados = intentosRealizados + 1
    if adivinar < número:
        print("estas muy lejos.") 
    if adivinar > número:
        print("estas muy cerca.")
    if adivinar == número:
        break
if adivinar == número:
    print("¡Has adivinado mi número en", intentosRealizados, " intentos!")
if adivinar != número:
    print("no has adivinado. El número que estaba pensando era",  número)