#정렬
n = int(input())
dic = [[] for _ in range(51)]
ans = []

for _ in range(n):
    serial = input()
    num = 0
    for s in serial:
        if s.isdigit():
            num += int(s)
    dic[len(serial)].append((num, serial))
    dic[len(serial)].sort(key=lambda x:(x[0], x[1]))


for words in dic:
    if words:
        for info in words:
            ans.append(info[1])

for an in ans:
    print(an)