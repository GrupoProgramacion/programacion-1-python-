# promedio
from functools import reduce 

n = int(input())
x = list(map(lambda x: int(input()), range(1,n+1)))

promedio = reduce(lambda x , y : (x + y )/ 2, x)

print(max(x))
print(min(x))
print(int(round(promedio,0)))

