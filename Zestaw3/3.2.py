# zadanie 3.2
print "Zadanie 3.2"

# zmienna L nie zdefiniowana
#L = L.sort()

# przypisanie 3 wartosci 2 zmiennym
#x, y = 1, 2, 3

# X jest krotka, niemodyfikowalna
#X = 1, 2, 3 ; X[1] = 4

# X jest lista 3-elementowa a probujemy przypisac do czwartego
#X = [1, 2, 3] ; X[3] = 4

#stringi sa niezmienne
#X = "abc" ; X.append("d")

# pow to metoda przyjmujaca 2 argumenty
#map(pow, range(8))

# mozemy to zrobic np tak:
def power(T):
    return (pow(2,T))

print map(power, range(8))

