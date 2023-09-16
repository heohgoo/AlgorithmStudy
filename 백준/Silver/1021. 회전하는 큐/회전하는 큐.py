import sys
input = sys.stdin.readline

def rotate_left(arr):
    tmp = []
    tmp += arr[1:]
    tmp.append(arr[0])
    return tmp

def rotate_right(arr):
    tmp = []
    tmp.append(arr[-1])
    tmp += arr[:len(arr)-1]
    return tmp

n, m = map(int, input().split())
nums = list(map(int, input().split()))
q = [i for i in range(1, n+1)]
ans = 0

for num in nums:
    idx = q.index(num)
    if len(q)-idx >= idx+1:
        while q[0] != num:
            q = rotate_left(q)
            ans += 1
        q.pop(0)
    
    else:
        while q[0] != num:
            q = rotate_right(q)
            ans += 1
        q.pop(0)

print(ans)