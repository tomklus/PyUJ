# zadanie 3.9
print "\n Zadanie 3.9"

L = [[3],[4,5,7,4],[1,1,1,1],(5,5),(4,7,9)]
print L
print[ sum(seq,0) for seq in L]

# zadanie 3.10
print "\n Zadanie 3.10"

#D = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
D = dict(zip('MDCLXVI', (1000, 500, 100, 50, 10, 5, 1)))

def roman2int(roman):
    result = 0
    last = 0
    for x in reversed(roman):
        val = D[x]
        if val >= last:
            last = val
            result += val
        else:
            result -= val
    return result

print "MCMXCIV to " + str(roman2int("MCMXCIV"))
