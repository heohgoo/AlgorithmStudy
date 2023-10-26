#dp
n = int(input())
a = list(map(int, input().split()))
ans = 0
reverse_a = a[::-1]

arr = [1]*n
reverse_arr = [1]*n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]: #증가하는 순서대로
            arr[i] = max(arr[i], arr[j]+1)

        if reverse_a[i] > reverse_a[j]: #감소하는 순서대로
            reverse_arr[i] = max(reverse_arr[i], reverse_arr[j]+1)


for i in range(n):
    #해당 인덱스의 수가 한번 더 포함되므로, 1을 뺀다.
    ans = max(ans, arr[i]+reverse_arr[n-i-1]-1)

print(ans)