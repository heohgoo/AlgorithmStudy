# from itertools import combinations

# n = int(input())
# checkpoint = []
# combi = []
# result = float('inf')

# for _ in range(n):
#     x, y = map(int, input().split())
#     checkpoint.append((x, y))

# combi = list(combinations(checkpoint, len(checkpoint)-1))
# combi.pop()
# combi.pop(0)

# for c in combi:
#     tmp = 0
#     for i in range(1, len(c)):
#         tmp += abs(c[i][0] - c[i-1][0]) + abs(c[i][1] - c[i-1][1])
#     result = min(tmp, result)

# print(result)


n = int(input())
checkpoint = []
check = 0
total_sum = 0

for _ in range(n):
    x, y = map(int, input().split())
    checkpoint.append((x, y))

for i in range(n-1):
    total_sum += abs(checkpoint[i][0] - checkpoint[i+1][0]) + abs(checkpoint[i][1] - checkpoint[i+1][1])

for i in range(1, n-1):
    left_tmp = abs(checkpoint[i][0] - checkpoint[i-1][0]) + abs(checkpoint[i][1] - checkpoint[i-1][1])
    right_tmp = abs(checkpoint[i][0] - checkpoint[i+1][0]) + abs(checkpoint[i][1] - checkpoint[i+1][1])
    mid_tmp = abs(checkpoint[i-1][0] - checkpoint[i+1][0]) + abs(checkpoint[i-1][1] - checkpoint[i+1][1])
    tmp = left_tmp + right_tmp - mid_tmp
    check = max(tmp, check)

print(total_sum - check)