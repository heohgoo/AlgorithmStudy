#배열로 간단하게, remove 이용
n = int(input())
word = list(input())
answer = 0

for _ in range(n-1):
    cnt = 0
    target = word[:]
    cp = list(input())

    for c in cp:
        if c in target:
            target.remove(c)
        else:
            cnt += 1
    
    if len(target) <= 1 and cnt <= 1:
        answer += 1

print(answer)