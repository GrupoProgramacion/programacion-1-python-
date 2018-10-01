# promedio
from functools import reduce 

n = int(input())
x = list(map(lambda x: int(input()), range(1,n+1)))

promedio = reduce(lambda x , y : (x + y )/ 2, x)

print(max(x))
print(min(x))
print(int(round(promedio,0)))

x = int(input())

#PY1_Elif
def toString(n):
    if n == 0:
        return "cero"
    elif n == 1:
        return "uno"
    elif n == 2:
        return "dos"
    elif n == 3:
        return "tres"
    elif n == 4:
         return "cuatro"
    elif n == 5:
         return "cinco"
    elif n == 6:
         return "seis"
    elif n == 7:
         return "siete"
    elif n == 8:
         return "ocho"
    elif n == 9:
        return "nueve"
    elif n == 10:
        return "diez"
    else: 
        return "número no válido"
    
print(toString(x))

def esmult(x,y):
    if x % y == 0 :
        return True
    else :
        return False

def mainMultiploAdeB(x,y):
    if esmult(x,y) == True :
        return str(x) + " es multiplo de " + str(y)
    else :
        return str(x) + " no es multiplo de " + str(y)

print(mainMultiploAdeB(int(input()),int(input())))

def validInput():
    out = int(input())
    
    if out >= 3 :
        return out
    else :
        print("Error al ingresar los datos")
        raise SystemExit
        
def Dibujar(ancho,largo,borde,fondo):
    for y in range(0,ancho):
        for x in range(0,largo):
            if y == 0 or y == ancho :
                print(borde)
            else:
                print(fondo)
    print("\n")
               
Dibujar(validInput(),validInput(),input(),input())

