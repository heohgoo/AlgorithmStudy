import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = map(int, input())
    record = list(map(int, input().split()))
    teams = []
    dict = {}
    info = []
    for r in set(record):
        if record.count(r) == 6:
            teams.append(r)
    
    score = 0
    for r in record:
        if r in teams:
            score += 1
            if r not in dict:
                dict[r] = [score]
            else:
                dict[r] += [score]
    

    for team in dict:
        team_sum = sum(dict[team][:4])
        five = dict[team][4]
        info.append([team, team_sum, five])
    
    info.sort(key=lambda x:(x[1], x[2]))
    print(info[0][0])