#백트래킹(DFS), N-Queen
n = int(input())

cnt = 0
where = [0]*n

def possible(num):
    for i in range(num):
        if where[i] == where[num] or abs(num-i) == abs(where[num]-where[i]):
            return False
    return True

def dfs(num):
    global cnt
    if num == n:
        cnt += 1
        return
    for i in range(n):
        where[num] = i
        if possible(num):
            dfs(num+1)

dfs(0)
print(cnt)