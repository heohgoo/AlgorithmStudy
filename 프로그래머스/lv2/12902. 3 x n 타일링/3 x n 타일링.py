#점화식
def solution(n):
    exp = [0, 3, 11] #0, 2, 4
    idx = int(n/2)
    if n%2 == 1:
        return 0
    if n <= 4:
        return exp[idx]
    
    for i in range(3, idx+1):
        exp.append((3*exp[i-1]+2*sum(exp[1:i-1])+2)%1000000007)

    return exp[-1]
    