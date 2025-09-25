
import math

def prime(x):
    if x < 2:
        return(False)
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return(False)
    return(True)

primes = []

squares = []

for i in range(10000):
    if prime(i):
        primes.append(i)

for i in range(10000):
    squares.append(i**2)

for i in range(1, 50000, 2):
    able = False
    for j in primes:
        for k in squares:
            if j + 2*k == i:
                able = True
                break
        if able == True:
            break
    if able == False:
        print(i)

