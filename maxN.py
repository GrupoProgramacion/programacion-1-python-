from functools import reduce

n = int(input())
x = list(map(lambda x: int(input()), range(1,n+1)))

def maximo(lista):
    return reduce(lambda x , y:x if x > y else y , lista)

print(maximo(x))
