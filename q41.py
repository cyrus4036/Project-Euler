from itertools import permutations

import math

def prime(x):
    if x < 2:
        return(False)
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return(False)
    return(True)



digits = [1,2,3,4,5,6,7,8,9]

digits = [1,2,3,4,5,6,7,8]

nums = list(permutations(digits))


for i in range(len(nums)-1,0,-1):
    curr = ''
    for j in range(len(nums[i])):
        curr = curr + str(nums[i][j])
    curr = int(curr)
    if prime(curr):
        print(curr)
        break
