#슬라이딩 윈도우
string = list(input())
a_cnt = string.count('a')
ans = float('inf')
start = 0

while start < len(string):
    end = start + a_cnt

    if end < len(string):
        tmp = string[start:end].count('b')
    else:
        tmp = (string[start:len(string)] + string[:end-len(string)]).count('b')
    
    start += 1
    ans = min(ans, tmp)

print(ans)