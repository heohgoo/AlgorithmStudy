def convert(num, n):
    result = ''   
    string = '0123456789ABCDEF'
    
    if num == 0:
        return '0'
    
    while num > 0:
        num, mod = divmod(num, n)
        result += string[mod]
    
    return result[::-1]


def solution(n, t, m, p):
    answer = ''
    string = ''
    for i in range(m*(t-1)+p):
        string += convert(i, n)
    
    for i in range(t):
        answer += string[m*i+p-1]
        
    return answer