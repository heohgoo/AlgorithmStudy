#구현
import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    n, k, t, m = map(int, input().split())
    info = {x:[0, 0, 0] for x in range(1, n+1)} #제출 시간, 제출 횟수, 최종 점수
    score = {x:[0]*(k+1) for x in range(1, n+1)}

    for time in range(1, m+1):
        team_id, pro_id, s = map(int, input().split())
        if score[team_id][pro_id] < s:
            score[team_id][pro_id] = s
        info[team_id][0] = time
        info[team_id][1] += 1
    
    
    for i in range(1, n+1):
        info[i][2] = sum(score[i])
    
    result = list(info.items())
    result.sort(key = lambda x : (-x[1][2], x[1][1], x[1][0]))

    for i in range(len(result)):
        if result[i][0] == t:
            print(i+1)