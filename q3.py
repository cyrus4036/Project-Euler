
import math

#defining variables

factors = []

num = 600851475143

largest = 0


#checking all the factors of the number

for i in range(2, int(math.sqrt(num))+1):
    if num%i == 0:
        factors.append(i)
        factors.append(num//i)

#checking which factors are prime


for i in range(0, len(factors)):
    check = factors[i]
    prime = True
    for j in range(2, int(math.sqrt(check))+1):
        if check%j == 0:
            prime = False
            break
    if prime == True:
        largest = check

print(largest)
            



print(factors)
            
