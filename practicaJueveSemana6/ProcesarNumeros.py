from functools import reduce

def inputLista():
    a = 1
    out = []
    while a != 0:
        out.append(a)
        a = validInput("ingrese un numero")
    return out

def validInput(cadena):
   n = int(input(cadena))

   if n < 0 or n > 1000:
       print("Invalid input")
       raise SystemExit
   elif n == 0 :
    break
   else :
      return n

def odd(n):
    if n % == 0:
        return False
    else:
        return True

lista = inputLista()

n = len(lista)
numeroImpares = reduce(lambda x,y : odd(x)+y,lista)
numeroPares = n - numeroImpares

print(n)
print(numeroPares)
print(numeroImpares)

"""
Realice un programa, que permita al usuario ingresar varios números () enteros hasta que introduzca el numerocero.

Luego mostrar lo siguiente:

La cantidad de números leídos, sin incluir al cero. La cantidad de números pares La cantidad de números impares

Input Format

Cada línea representa un número

Constraints

Output Format

Si las entradas no son correctas, mostrar "Invalid input". En caso contrario: La cantidad de números leídos, sin incluir al cero. La cantidad de números pares La cantidad de números impares

Sample Input 0

1
1
1
0

Sample Output 0

3
0
3
"""
