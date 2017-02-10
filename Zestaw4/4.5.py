def odwracanie(L,left,right):
    for i in range((right-left+1)/2):
        x = L[left+i]
        L[left+i] = L[right-i]
        L[right-i] = x 
    return L

def odwracanie_rek(L,left,right):
    if left >= right : return L
    L[left], L[right] = L[right], L[left]
    return odwracanie_rek(L, left+1, right-1)
    
        


L = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

print odwracanie(L,1,13)

L = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

print odwracanie_rek(L,1,13)
