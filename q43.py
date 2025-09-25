from itertools import permutations

nums = list(permutations(['0','1','2','3','4','5','6','7','8','9']))

total = 0

for i in nums:
    while True:
        if int(i[7]+i[8]+i[9])%17 != 0:
            break
        if int(i[6]+i[7]+i[8])%13 != 0:
            break
        if int(i[5]+i[6]+i[7])%11 != 0:
            break
        if int(i[4]+i[5]+i[6])%7 != 0:
            break
        if int(i[3]+i[4]+i[5])%5 != 0:
            break
        if int(i[2]+i[3]+i[4])%3 != 0:
            break
        if int(i[1]+i[2]+i[3])%2 != 0:
            break
        total += int(i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6]+i[7]+i[8]+i[9])
        print(int(i[0]+i[1]+i[2]+i[3]+i[4]+i[5]+i[6]+i[7]+i[8]+i[9]))
        break
print(total)