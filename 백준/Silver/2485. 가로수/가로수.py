#최대공약수, 유클리드 호제
def gcd(a, b):
    while True:
        if a % b == 0:
            return b
        r = a % b
        a, b = b, r

n = int(input())
trees = []
ans = 0

for _ in range(n):
    trees.append(int(input()))

first = trees[1] - trees[0]
for i in range(2, n):
    second = trees[i] - trees[i-1]
    first = gcd(second, first)

for i in range(1, n):
    ans += (trees[i] - trees[i-1]) // first - 1

print(ans)