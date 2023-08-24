#슬라이딩 윈도우
import sys
input = sys.stdin.readline

n, window = map(int, input().split())
visit_list = list(map(int, input().split()))
visitor_list = []

def solve():
    answer = sum(visit_list[:window])
    visitor_list.append(answer)

    for i in range(window, n):
        answer -= visit_list[i-window]
        answer += visit_list[i]
        visitor_list.append(answer)

solve()

if max(visitor_list) == 0:
    print("SAD")
else:
    print(max(visitor_list))
    print(visitor_list.count(max(visitor_list)))