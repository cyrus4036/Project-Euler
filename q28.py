diagonals = []

curr = 0
spacing = 2


initial = 1

length = 1001


while len(diagonals) < length*2-1:
    for i in range(initial, length**2+1,spacing):
        curr += 1
        if curr % 5 == 0:
            spacing += 2
            initial = i
            break
        diagonals.append(i)

total = 0

for i in diagonals:
    total += i
print(total)

