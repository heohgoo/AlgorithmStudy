def divisorandmax(n):
    if n == 1:
        return 0
    result = [1]
    
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0 and i <= 1e7:
            result.append(i)
            if n // i != n and n // i <= 1e7:
                result.append(n//i)
    return max(result)
    

def solution(begin, end):
    result = []
    for i in range(begin, end+1):
        result.append(divisorandmax(i))
    return result
    