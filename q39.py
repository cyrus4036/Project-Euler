triples = set()


for k in range(1,100):
    for i in range(1, 100):
        for j in range(1,i):
            curr = (k*(i**2-j**2),k*(2*i*j),k*(i**2+j**2))
            curr = sorted(curr)
            curr = tuple(curr)
            triples.add(curr)

maximum = 0
current = 0
triples = sorted(triples)

for i in range(1000):
    total = 0
    for j in triples:
        if j[0]+j[1]+j[2] == i:
            total += 1
    if total > maximum:
        maximum = total
        current = i




print(current,maximum)
