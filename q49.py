
import math

from itertools import permutations

def prime(x):
    if x < 2:
        return(False)
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return(False)
    return(True)


fourdigitprimes = []

for i in range(1000,10000):
    if prime(i):
        fourdigitprimes.append(i)



for i in fourdigitprimes:
    digits = []
    num = str(i)
    permutes = []
    for j in range(len(num)):
        digits.append(num[j])
    possibles = list(permutations(digits))
    for j in range(len(possibles)):
        curr = ''
        for k in range(len(possibles[j])):
            curr = curr + possibles[j][k]
        curr = int(curr)
        possibles[j] = curr
    for j in fourdigitprimes:
        for k in possibles:
            if j == k:
                permutes.append(j)
    total = 0
    permutes = sorted(permutes)
    for i in permutes:
        for j in permutes:
            for k in permutes:
                if abs(i-j) == abs(j-k) and i!=j and j!=k and i!=k:
                    print(i,j,k)



                
