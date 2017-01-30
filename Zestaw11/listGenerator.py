import random
import math
import cmath

def swap(L, left, right):
    """Zamiana miejscami dwoch elementow na liscie."""
    item = L[left]
    L[left] = L[right]
    L[right] = item
    
    

def random_list(size, maxVal):
    return [random.randint(0,maxVal) for r in range(size)]

def nearly_sorted(size, maxVal):
    L = [random.randint(0,maxVal) for r in range(size)]
    print(L)
    for i in range(0,int(size/2)):
        k = i
        for j in range(i+1, size):
            if L[j] < L[k]:
                k = j
        swap(L, i, k)
    return L

def reverse_nearly_sorted(size, maxVal):
    L = [random.randint(0,maxVal) for r in range(size)]
    print(L)
    for i in range(0,int(size/2)):
        k = i
        for j in range(i+1, size):
            if L[j] > L[k]:
                k = j
        swap(L, i, k)
    return L

def gauss_random(size):
    L = [int(random.gauss(0,1)) for r in range(size)]
    return L

def random2(size):
    L = [random.randint(0,int(math.sqrt(size))) for r in range(size)]
    return L


print(random_list(10,50))
print(nearly_sorted(10,50))
print(reverse_nearly_sorted(10,50))
print(gauss_random(10))
print(random2(10))

