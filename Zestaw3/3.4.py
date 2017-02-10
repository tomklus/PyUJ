# zadanie 3.4
print "\n Zadanie 3.4"


while True:
    napis = str(raw_input("Podaj liczbe rzeczywista lub stop aby skonczyc \n"))

    if napis == "stop":
        break

    elif napis.isdigit():
        liczba = int(napis)
        print "(%d,%d) %d" % (liczba,liczba, pow(2,liczba))

    else: print "Podales: %s a to nie liczba rzeczywista! Sprobuj jeszcze raz \n" % (napis)


