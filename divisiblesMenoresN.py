from functools import reduce

n = int(input())
x = int(input())

def diviblesMenoresN(lista,divisor):
   return list(filter(lambda x: x % divisor == 0, lista))

print(*diviblesMenoresN(range(1,n),x),sep='\n')
