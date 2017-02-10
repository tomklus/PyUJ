line = "siekiera motyka baba gola rowerek"

S = [ w [:1] for w in line.split()]
print "".join(S)
S = [ w [-1] for w in line.split()]
print "".join(S)

