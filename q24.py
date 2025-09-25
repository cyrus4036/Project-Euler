from itertools import permutations


permutes = permutations([0,1,2,3,4,5,6,7,8,9])

permutes = sorted(permutes)

print(permutes[999999])