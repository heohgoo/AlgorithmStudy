#백트래킹, permutation
from itertools import permutations

n, m = map(int, input().split())
num = [i for i in range(1, n+1)]
result = list(permutations(num, m))

for i in range(len(result)):
    for j in range(len(result[0])):
        print(result[i][j], end=' ')
    print()