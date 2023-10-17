#백트래킹
n, s = map(int, input().split())
num_list = list(map(int, input().split()))
ans = 0

def dfs(idx, sub_sum):
    global ans

    if idx >= n:
        return
    
    sub_sum += num_list[idx]

    if sub_sum == s:
        ans += 1

    #해당 idx를 선택한 경우
    dfs(idx+1, sub_sum)

    #해당 idx를 선택하지 않는 경우
    dfs(idx+1, sub_sum - num_list[idx])

dfs(0, 0)
print(ans)