def linijka(dlugosc):
    jednostka = "|...."
    koniec = "|"
    miarka = jednostka * dlugosc + koniec

    podzialka = ""
    for item in range(dlugosc +1):
        if item == 9 :
            podzialka = podzialka + str(item).ljust(4)
        else:
            podzialka = podzialka + str(item).ljust(5)
    calosc = miarka + "\n" + podzialka
    return calosc

dlugosc = int(raw_input("Podaj dlugosc \n"))

print linijka(dlugosc)

def prostokat(wysokosc,dlugosc):
    jednostka = "+---"
    koniec = "+"
    bok = "|   "

    S = ""
    for item in range(wysokosc):
        S = S + jednostka * (dlugosc) + koniec + "\n" + bok * (dlugosc +1) + "\n"

    S = S + jednostka * (dlugosc) + koniec
    return S


dlugosc = int(raw_input("Podaj dlugosc \n"))

wysokosc = int(raw_input("Podaj wysokosc \n"))

print prostokat(wysokosc,dlugosc)
