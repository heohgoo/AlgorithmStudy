#dp
first = list(input())
second = list(input())
dp = [[0]*(len(second)+1) for _ in range(len(first)+1)]

for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        if first[i-1] == second[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])


ans = 0

for row in dp:
    ans = max(max(row), ans)

print(ans)

