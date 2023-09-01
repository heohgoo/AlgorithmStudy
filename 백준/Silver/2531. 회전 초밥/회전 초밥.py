#메모리 초과 해결
n, d, k, c = map(int, input().split())
belt = []
# situation = []
answer = 0

for _ in range(n):
    num = int(input())
    belt.append(num)

for i in range(n):
    if i+k <= n:
        tmp = belt[i:i+k]
        tmp = list(set(tmp))

        if c not in tmp:
            answer = max(answer, len(tmp)+1)
        else:
            answer = max(answer, len(tmp))
        # situation.append(list(set(tmp)))
        # if len(set(tmp)) == k:
        #     situation.append(tmp)

    else:
        tmp = belt[i:] + belt[:(i+k)-n]
        tmp = list(set(tmp))

        if c not in tmp:
            answer = max(answer, len(tmp)+1)
        else:
            answer = max(answer, len(tmp))
        # situation.append(list(set(tmp)))
        # if len(set(tmp)) == k:
        #     situation.append(tmp)


# for s in situation:
#     if c not in s:
#         answer = max(answer, len(s)+1)
#     else:
#         answer = max(answer, len(s))
print(answer)
