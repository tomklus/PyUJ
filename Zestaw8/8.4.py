import math
import copy


def heron(a, b, c):
    boki = [a, b, c]
    mnboki = copy.copy(boki)
    mnboki.remove(max(mnboki))
    print(boki)
    print(mnboki)

    if max(boki) < mnboki[0] + mnboki[1]:
        return math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / float(4)
    raise ValueError

print(heron( 1.2, 3, 4))
