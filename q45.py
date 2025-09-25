import math

#not efficient BF solution

def isTriangular(n):
    if (math.sqrt(1+8*n)-1) %2 == 0:
        return(True)
    else:
        return(False)

def isPentagonal(n):
    if (math.sqrt(1+24*n)+1) % 6 == 0:
        return(True)
    else:
        return(False)

def isHexagonal(n):
    if (math.sqrt(1+8*n)+1) % 4 == 0:
        return(True)
    else:
        return(False)

for i in range(10**10):
    if isPentagonal(i) and isHexagonal(i):
        print(i)