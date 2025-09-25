import math

# def factors(n):
#     f = []
#     for i in range(1, int(math.sqrt(n))+1):
#         if n%i == 0:
#             f.append(i)
#             f.append(n//i)
#         if math.sqrt(n) == float(i):
#             f.remove(i)
#     return(f)

# abundants = []

# for i in range(11,28123):
#     curr = factors(i)
#     curr.remove(i)
#     factorsum = 0
#     for j in curr:
#         factorsum += j
#     if factorsum > i:
#         abundants.append(i)


abundants = []
total = 0

with open('q23abundants.txt','r') as f:
    abundants = f.read().splitlines()
    abundants = list(map(int,abundants))


possibles = set()

for i in abundants:
    for j in abundants:
        if i+j < 28123:
            possibles.add(i+j)
        else:
            break



for i in range(28123):
    if i not in possibles:
        total += i
        print(i)

print(total)


