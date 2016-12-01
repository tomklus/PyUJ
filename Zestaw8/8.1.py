import fractions
def solve1(a, b, c):
    """Rozwiazywanie rownania liniowego a x + b y + c = 0."""
    print("rownanie: %fx + %fy + %f = 0" % (a, b, c))

    if a != 0 and b != 0 and c != 0:
        div = -1 * (a / b)
        div2 = -1 * (c / b)
        print("y = %.2fx %+.2f" % (div, div2))
        return


    elif a == 0:
        if b == 0:
            if c == 0:
                print("nieskonczona liczba rozwiazan")
                return

            print("Rownanie sprzeczne: %f = 0" % c)
            return

        print("x = 0")
        y = -c / float(b)
        print("y = %f" % y)
        return

    elif b == 0:
        print("y = 0")
        x = -c/float(a)
        print("x = %f" % x)



solve1(2, 1, -1)
