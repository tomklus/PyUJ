n = int(raw_input("Prosze podac liczbe: "))
def silnia(n):
    silnia_tmp = 1
    if n in (0,1):
        return 1
    else:
        for i in range(2,n+1):
            silnia_tmp = silnia_tmp*i
        return silnia_tmp

print silnia(n)
