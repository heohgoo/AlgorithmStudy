#조합, 완탐
from itertools import combinations

while True:
    s = []
    combi = []
    test_case = list(map(int, input().split()))
    if test_case[0] == 0:
        break
    k = test_case[0]
    s = test_case[1:]

    tmp = list(combinations(s, 6))
    for t in tmp:
        if t not in combi:
            combi.append(t)
    
    for c in combi:
        print(*c)
    print()