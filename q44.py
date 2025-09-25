pentagonals = []


import math

for i in range(10**7):
    if (math.sqrt(1+24*i) + 1) % 6 == 0:
        pentagonals.append(i)

def isPentagonal(n):
    if (math.sqrt(1+24*n)+1) % 6 == 0:
        return(True)
    else:
        return(False)
    

minimum = 10**10


for i in pentagonals:
    for j in pentagonals:
        if isPentagonal(i+j) and isPentagonal(abs(i-j)):
            print(i-j)
            if abs(i-j) < minimum:
                minimum = abs(i-j)
                print(i-j)

print(minimum)









