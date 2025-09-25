# A tool to check for the factors of a number

import math


def factors(n):
    f = []
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            f.append(i)
            f.append(n//i)
    return(f)


print(factors(28))
