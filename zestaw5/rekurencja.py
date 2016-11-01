import sys

def silnia(n):
    silnia_tmp = 1
    if n in (0,1):
        return 1
    else:
        for i in range(2,n+1):
            silnia_tmp = silnia_tmp*i
        return silnia_tmp
        
        
def fib(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
    
