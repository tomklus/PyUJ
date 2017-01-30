import listGenerator


def moda_py(L):

    occurrences = {}
    for number in L:
        if number in occurrences:
            occurrences[number] += 1
        else:
            occurrences[number] = 1

    v = list(occurrences.values())
    k = list(occurrences.keys())
    print(occurrences)
    print("dominanta:%s %sx" % (k[v.index(max(v))], v[v.index(max(v))] ))


L = listGenerator.random_list(100, 100)
moda_py(L)
