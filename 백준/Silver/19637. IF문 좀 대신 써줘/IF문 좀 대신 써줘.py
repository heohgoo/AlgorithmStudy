#이진 탐색
import sys
input = sys.stdin.readline


def binary(p):
    left = 0
    right = len(power_list)-1

    while left <= right:
        mid = (left + right) // 2
        if p > power_list[mid]:
            left = mid + 1
        else:
            right = mid - 1
    
    return name_list[right + 1]


n, m = map(int, input().split())
power_list = []
name_list = []

for i in range(n):
    name, power = input().split()
    power = int(power)

    if power_list and power_list[-1] == power: #처음 칭호만 저장한다.
        continue

    power_list.append(power)
    name_list.append(name)

for _ in range(m):
    cha = int(input())
    print(binary(cha))
