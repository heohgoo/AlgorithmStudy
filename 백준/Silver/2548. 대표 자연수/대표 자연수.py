#분산이 제일 작은 경우
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

if n % 2 == 0:
    print(n_list[(n//2)-1])
else:
    print(n_list[(n//2)])