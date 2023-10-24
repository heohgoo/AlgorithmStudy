#이분탐색
n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)

while start <= end:
    mid = (start + end) // 2
    cut_tree = 0 
    for tree in trees:
        if mid < tree:
            cut_tree += tree - mid

    if cut_tree >= m:
        start = mid + 1

    else:
        end = mid - 1 

print(end)