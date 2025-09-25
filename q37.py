
import math

def prime(x):
    if x < 2:
        return(False)
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return(False)
    return(True)

works = []

for i in range(10,1000000):
    i = str(i)
    trunc = True
    #deleting from right to left
    for j in range(len(i),0,-1):
        curr = int(i[:j])
        if not prime(curr):
            trunc = False
            break
    #deleting from left to right
    for j in range(len(i)):
        curr = int(i[j:])
        if not prime(curr):
            trunc = False
            break
    if trunc:
        works.append(int(i))

print(len(works))

total = 0

for i in works:
    total += i
print(total)

