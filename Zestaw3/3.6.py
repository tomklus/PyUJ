# zadanie 3.6
print "\n Zadanie 3.6"


dlugosc = int(raw_input("Podaj dlugosc \n"))

wysokosc = int(raw_input("Podaj wysokosc \n"))

jednostka = "+---"
koniec = "+"
bok = "|   "

S = ""
for item in range(wysokosc):
    S = S + jednostka * (dlugosc) + koniec + "\n" + bok * (dlugosc +1) + "\n"

S = S + jednostka * (dlugosc) + koniec
print S


