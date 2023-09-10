#백트래킹
def calc(a, b, op):
    if op == '<':
        if a >= b:
            return False
    
    if op == '>':
        if a <= b:
            return False
    
    return True

def dfs(cnt, arr):
    if cnt == k+1: #숫자가 다 차면
        answer.append(arr)
        return
    
    for i in range(10):
        if visited[i]:
            continue

        if cnt == 0 or calc(arr[-1], str(i), ops[cnt-1]):
            visited[i] = True
            dfs(cnt+1, arr+str(i))
            visited[i] = False 

k = int(input())
ops = list(input().split())
visited = [False]*10
answer = []
dfs(0, '')
print(answer[-1])
print(answer[0])