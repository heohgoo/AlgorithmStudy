#슬라이딩 윈도우
def isTrue(arr1, arr2):
    for i in range(4):
        if arr1[i] > arr2[i]:
            return False
    return True

s, p = map(int, input().split())
dna = list(input())
condition = list(map(int, input().split())) #A, C, G, T
compare = [0]*4
ans = 0

password = dna[:p]

for w in password:
    if w == 'A':
        compare[0] += 1
    elif w == 'C':
        compare[1] += 1
    elif w == 'G':
        compare[2] += 1
    else:
        compare[3] += 1

if isTrue(condition, compare):
    ans += 1

for i in range(p, s):
    if dna[i-p] == 'A':
        compare[0] -= 1
    elif dna[i-p] == 'C':
        compare[1] -= 1
    elif dna[i-p] == 'G':
        compare[2] -= 1
    else:
        compare[3] -= 1   
    

    if dna[i] == 'A':
        compare[0] += 1
    elif dna[i] == 'C':
        compare[1] += 1
    elif dna[i] == 'G':
        compare[2] += 1
    else:
        compare[3] += 1
    
    if isTrue(condition, compare):
        ans += 1

print(ans)
