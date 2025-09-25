
total = 0

for i in range(1000000):
    tens = str(i)
    binary = bin(i)[2:]
    tpalindrome = True
    bpalindrome = True
    for j in range(0,len(tens)//2):
        if tens[j] != tens[len(tens)-j-1]:
            tpalindrome = False
            break
    for j in range(0,len(binary)//2):
        if binary[j] != binary[len(binary)-j-1]:
            bpalindrome = False
            break
    if tpalindrome and bpalindrome:
        print(i)
        print(tens)
        print(binary)
        total += i

print(total)
