#슬라이딩 윈도우
def isTrue(arr1, arr2):
    for i in range(4):
        if arr1[i] > arr2[i]:
            return False
    return True

s, p = map(int, input().split())
dna = list(input())
condition = list(map(int, input().split())) #A, C, G, T
compare = {'A':0, 'C':0, 'G':0, 'T':0}
ans = 0

password = dna[:p]

for w in password:
    compare[w] += 1

if isTrue(condition, list(compare.values())):
    ans += 1

for i in range(p, s):
    compare[dna[i-p]] -= 1
    compare[dna[i]] += 1
    if isTrue(condition, list(compare.values())):
        ans += 1

print(ans)