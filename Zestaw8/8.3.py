import random
"""
3.6
3.08
3.092
3.142
3.1422
3.141512
3.1401636
3.14184416  10^8 losowan
"""

def in_circle(x, y):
    return x ** 2 + y ** 2 < 1


def calc_pi(n=100):
    inside_count = 0
    for _ in range(n):
        if in_circle(random.random(), random.random()):
            inside_count += 1

    pi = (inside_count / float(n)) * 4
    print (pi)


calc_pi(10)
calc_pi(10**2)
calc_pi(10**3)
calc_pi(10**4)
calc_pi(10**5)
calc_pi(10**6)
calc_pi(10**7)
calc_pi(10**8)

