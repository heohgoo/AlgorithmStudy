from itertools import permutations

n, k = map(int, input().split())
order = [i for i in range(n)]
gym = list(map(int, input().split()))

for i in range(len(gym)):
    gym[i] -= k

perm = list(permutations(order, n))
answer = 0

for p in perm:
    tmp = 0
    flag = True
    for i in range(n):
        tmp += gym[p[i]]
        if tmp < 0:
            flag = False
            break
    
    if flag:
        answer += 1

print(answer)