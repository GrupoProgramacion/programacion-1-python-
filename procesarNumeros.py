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
