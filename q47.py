import math



def prime(x):
    if x < 2:
        return(False)
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return(False)
    return(True)


def primefactors(n):
    if n == 0 or n == 1:
        return(1)
    curr = n
    facs = []
    while curr != 1:
        j = 2
        while True:
            if curr%j == 0 and prime(j):
                facs.append(j)
                curr = curr//j
                break
            j+= 1
    return(facs)


i = 2

while True:
    print(i)
    dpf1 = set(primefactors(i))
    dpf2 = set(primefactors(i+1))
    dpf3 = set(primefactors(i+2))
    dpf4 = set(primefactors(i+3))

    if len(dpf1) == 4 and len(dpf2) == 4 and len(dpf3) == 4 and len(dpf4) == 4:
        print(i, i+1,i+2,i+3)
        break
    i += 1


