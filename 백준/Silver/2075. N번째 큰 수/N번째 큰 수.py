from heapq import heappush, heappop

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
num_list = []

for i in range(n):
    for j in range(n):
        if len(num_list) < n:
            heappush(num_list, grid[i][j])
            continue

        if len(num_list) == n:
            if grid[i][j] > num_list[0]:
                heappop(num_list)
                heappush(num_list, grid[i][j])



print(num_list[0])