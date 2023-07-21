def cantour(i):
    if i % 5 == 2:
        return False
    
    if i < 5:
        return True
    
    return cantour(i//5)


def solution(n, l, r):
    answer = 0
    
    for i in range(l-1, r):
        if cantour(i):
            answer += 1
    
    return answer