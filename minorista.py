from functools import reduce

def valid(n):
   if n < 0 or n > pow(10,2):
       print("Invalid input")
       raise SystemExit
   else :
       return n

n = int(input())
x = list(map(lambda x: valid(int(input())), range(1,n+1)))

def peso(n):
   if n == 0:
       return 75
   else:
       return 112

def minorista(lista1):
     pesos = list(map(peso,lista1))
     return reduce(lambda x, y: x + y,pesos)

print(minorista(x))
