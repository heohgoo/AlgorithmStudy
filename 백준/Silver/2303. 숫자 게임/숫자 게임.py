from itertools import combinations

n = int(input())

pair = []
for i in range(n):
    max_sum = 0 
    n_list = list(map(int, input().split()))
    combi = list(combinations(n_list, 3))
    for c in combi:
        tmp = sum(c)
        max_sum = max(max_sum, tmp%10)
    
    pair.append((i+1, max_sum))

pair.sort(key=lambda x:(x[1], x[0]), reverse=True)
print(pair[0][0])