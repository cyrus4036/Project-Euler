#A tool to check if a number is prime
import math

def prime(x):
    if x < 2:
        return(False)
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return(False)
    return(True)

