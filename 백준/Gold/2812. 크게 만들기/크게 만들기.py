#그리디
n, k = map(int, input().split())
nums = input()

answer = []

for num in nums:
    while answer and int(answer[-1]) < int(num) and k > 0:
        answer.pop()
        k -= 1
    answer.append(num)

if k > 0:
    print(''.join(answer[:-k]))
else:
    print(''.join(answer))  