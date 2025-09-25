
cons = ""

i = 0

while len(cons) < 1000005:
    i = str(i)
    for j in range(0,len(i)):
        cons = cons + i[j]
    i = int(i) + 1

print(int(cons[1])*int(cons[10])*int(cons[100])*int(cons[1000])*int(cons[10000])*int(cons[100000])*int(*cons[1000000]))