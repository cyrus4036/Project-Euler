total = 0


import math

def prime(x):
    if x < 2:
        return(False)
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return(False)
    return(True)

def rotate(x):
    curr = x
    curr.insert(0,x[len(x)-1])
    del curr[len(curr)-1]
    return(curr)





total = 0

for i in range(1000000):
    num = str(i)
    numList = []
    for j in range(len(num)):
        numList.append(num[j])
    circles = []
    circles.append(numList)
    for j in range(len(numList)):
        numList = rotate(numList)
        circles.append(numList.copy())
    del circles[0]

    circular = True
    for j in range(len(circles)):
        curr = ''
        for k in range(len(circles[j])):
            curr = curr + circles[j][k]
        curr = int(curr)
        if not prime(curr):
            circular = False
            break
    if circular:
        total += 1
        print(i)

print(total)


        







