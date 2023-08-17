#그리디
#0은 뒤부터, 1은 앞부터 지운다.
string = list(input())
zero = string.count('0')//2
one = string.count('1')//2

for _ in range(zero):
    string.pop(-string[::-1].index('0')-1)

for _ in range(one):
    string.pop(string.index('1'))

print("".join(string))