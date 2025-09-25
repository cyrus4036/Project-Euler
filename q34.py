def factorial(n):
    if n == 0:
        return(1)
    return(n*factorial(n-1))

print(145+40585)


for i in range(3, 2000000):
    num = str(i)
    digits = []
    facsum = 0
    for j in range(len(num)):
        digits.append(num[j])
    for j in digits:
        facsum += factorial(int(j))
    if facsum == i:
        print(i)
