def odwracanie(L,left,right):
    for i in range((right-left+1)/2):
        x = L[left+i]
        L[left+i] = L[right-i]
        L[right-i] = x 
   	print L
    return L

def odrwacanie_rek(L.left,right):
    


L = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

print odwracanie(L,3,10)
