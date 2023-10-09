#구현
import copy

def combinations(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        elem = arr[i]
        for j in combinations(arr[i+1:], n-1):
            result += [[elem]+j]
    return result

def attack(arr):
    attack_info = []
    cnt = 0

    for archer in arr:
        pos = []
        for i in range(n):
            for j in range(m):
                if tmp[i][j]: #적이 있다면
                    cur_d = abs(n-i) + abs(j-archer)
                    if cur_d <= d:
                        pos.append((cur_d, i, j))
        pos.sort(key=lambda x:(x[0], x[2]))

        if pos:
            attack_info.append(pos[0])
    
    for a in attack_info:
        _, i, j = a
        if tmp[i][j] == 1:
            tmp[i][j] = 0
            cnt += 1
    
    return cnt


def move():
    for i in range(n-1, 0, -1):
        tmp[i] = tmp[i-1]
    
    tmp[0] = [0]*m


def is_empty():
    for i in range(n):
        for j in range(m):
            if tmp[i][j]:
                return False
    return True

  
n, m, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
castle = [i for i in range(m)]
ans = 0

for archers in combinations(castle, 3):
    tmp = copy.deepcopy(grid) #grid 보존
    cnt = 0
    while not is_empty():
        cnt += attack(archers)
        move()
    ans = max(cnt, ans)

print(ans)