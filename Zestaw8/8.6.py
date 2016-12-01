results = {(0, 0): 0.5}


def count_P(a, b):

    global results

    if (a, b) not in results:

        if b == 0 and a > 0:
            results[(a, b)] = 0.0

        elif a == 0 and b > 0:
            results[(a, b)] = 1.0

        elif a > 0 and b > 0:
            results[(a, b)] = 0.5 * (count_P(a - 1, b) + count_P(a, b - 1))

        else:
            raise ValueError("(a or b) < 0 -> a = %f b = %f" % (a, b))

    return results[(a, b)]

count_P(2,6)
print (results[(2, 6)])
