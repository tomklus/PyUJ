# zadanie 3.5
print "\n Zadanie 3.5"

jednostka = "|...."
koniec = "|"

dlugosc = int(raw_input("Podaj dlugosc \n"))
miarka = jednostka * dlugosc + koniec

podzialka  = ""
for item in range(dlugosc +1):
    if item == 9 :
        podzialka = podzialka + str(item).ljust(4)
    else:
        podzialka = podzialka + str(item).ljust(5)
calosc = miarka + "\n" + podzialka
print calosc


