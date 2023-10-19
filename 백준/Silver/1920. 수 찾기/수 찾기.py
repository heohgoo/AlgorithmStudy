#이분탐색
#O(NlogN)
n = int(input())
a = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
a.sort() #오름차순 정렬


for num in arr:
    start, end = 0, n-1
    isTrue = False

    while start <= end:
        mid = (start + end) // 2
        if num == a[mid]:
            isTrue = True
            print(1)
            break
    
        elif num > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    
    if not isTrue:
        print(0)