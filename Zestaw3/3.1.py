# zadanie 3.1
print "Zadanie 3.1"
# kod dziala, ale sredniki nie powinny byc w if,else
x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;
print result

# brakowalo wciecia
for i in "qwerty":
    if ord(i) < 100: print i


# poprawny kod skladniowo
for i in "axby": print ord(i) if ord(i) < 100 else i

