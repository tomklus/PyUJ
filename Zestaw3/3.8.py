# zadanie 3.8
print "\n Zadanie 3.8"

A = ["e","a","b","c","d","e","f","g"]
B = ["e","f","x","d","m","n","z"]

L = []
# iloczyn list
print A
print B
for item in A:
    if item in B:
       if item not in L:
           L.append(item)
print L
# suma list
for item in A.__add__(B):
    if item not in L:
        L.append(item)
print L


