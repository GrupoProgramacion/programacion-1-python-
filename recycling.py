def validx(x):
   if x <= 0 or x >= 100:
       print("Invalid input")
       raise SystemExit
   else :
       return x

def validn(n):
   if n <= 1 or n >= 10:
       print("Invalid input")
       raise SystemExit
   else :
       return n

n = validn(int(input()))
x = list(map(lambda x: validx(float(input())), range(1,n+1)))

def precio(n):
   if n <= 1:
       return 0.10
   else:
       return 0.25

def reembolso(lista1):
     montos = list(map(precio,lista1))
     return reduce(lambda x, y: x + y,montos)

mireembolso = round(reembolso(x),2)

print(mireembolso)
