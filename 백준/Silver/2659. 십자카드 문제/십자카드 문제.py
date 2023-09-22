from collections import deque

def find_clock_num(n):
    n = deque(n)
    num = 10000
    for _ in range(4):
        now = n[0]*1000 + n[1]*100 + n[2]*10 + n[3]
        if now < num:
            num = now
        n.rotate(1)
    return num

n_list = list(map(int, input().split()))
clock_number = find_clock_num(n_list)

cnt = 0
start = 1111

while start <= clock_number:
    if find_clock_num(list(map(int, list(str(start))))) == start:
        cnt += 1
    start += 1

print(cnt)