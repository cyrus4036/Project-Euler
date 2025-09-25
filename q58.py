

diagonals = []

curr = 0
spacing = 2

length = 26589

initial = 1

import math

def prime(x):
    if x == 1:
        return(False)
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return(False)
    return(True)

ratio = 1

num = 1

while ratio >= 0.1:
    length += 1
    # curr += 1
    # while curr%5 != 0:
    #     curr += 1
    #     diagonals.append(num)
    #     num += spacing
    # spacing += 2

    while len(diagonals) < length*2-1:
        for i in range(initial, length**2+1,spacing):
            curr += 1
            if curr % 5 == 0:
                spacing += 2
                initial = i
                break
            diagonals.append(i)

    primetotal = 0

    for i in diagonals:
        if prime(i):
            primetotal += 1


    ratio = primetotal/len(diagonals)
    print(ratio)

print(ratio)
print(length)
        

# primetotal = 0

# for i in diagonals:
#     if prime(i):
#         primetotal += 1


# print(primetotal/len(diagonals))
    

    
