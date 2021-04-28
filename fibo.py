import math 
  
n=int(input())
def sq(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  
def fibcal(n):
    return sq(5*n*n + 4) or sq(5*n*n - 4) 
     
if (fibcal(n) == True):
    print(n,"is a Fibonacci Number")
else:
    print(n,"is a not Fibonacci Number")

