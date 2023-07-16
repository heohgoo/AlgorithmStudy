MAX = 1000000

def solution(n):
    answer = 0
    count = 0
    bin_n = bin(n)[2:]
    
    for i in range(len(bin_n)):
        if int(bin_n[i]) == 1:
            count += 1
    # print(bin(2)[2:])
    
    for i in range(n+1, MAX+1):
        num = bin(i)[2:]
        tmp = 0
        for j in range(len(num)):
            if int(num[j]) == 1:
                tmp += 1
        
        if tmp == count:
            return i
        
    return answer