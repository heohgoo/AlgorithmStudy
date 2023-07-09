def solution(arr):
    tmp = arr[0]
    
    for num in arr[1:]:
        if num % tmp == 0:
            tmp = num
            continue
        if num % tmp != 0 and tmp % num != 0:
            for i in range(2, tmp+1):
                mul = num*i
                if mul % tmp == 0:
                    tmp = mul
                    break
    return tmp