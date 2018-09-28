“””” 
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


…
“”” 

from functools import reduce

def validInput():
   n = int(input)
   
   if n < 0 or n > 1000:
       print("Invalid input")
       raise SystemExit
   elif n == 0 :
    break
   else :
      return n

n = int(input())
x = list(map( validInput , range(1,10000)))

print(len(x))
