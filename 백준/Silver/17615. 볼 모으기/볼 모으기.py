n = int(input())
balls = input()
ball_list = []

idx = 0
tmp = ''

while idx < n:
    if tmp == '':
        tmp += balls[idx]
        idx += 1
        continue

    if tmp[-1] == balls[idx]:
        tmp += balls[idx]
    
    else:
        ball_list.append(tmp)
        tmp = ''
        tmp += balls[idx]
    
    if idx == n-1 and tmp != '':
        ball_list.append(tmp)
    
    idx += 1

def solve(arr):
    odd_sum, even_sum = 0, 0

    if len(arr) == 1 or len(arr) == 2:
        return 0
    
    if len(arr) % 2 == 0:
        for i in range(1, len(arr)-2, 2):
            odd_sum += len(ball_list[i])
        
        for i in range(2, len(arr)-1, 2):
            even_sum += len(ball_list[i])
        
        return min(odd_sum, even_sum)
    
    else:
        for i in range(1, len(arr)-1, 2):
            odd_sum += len(ball_list[i])
        
        for i in range(0, len(arr)-2, 2):
            even_sum += len(ball_list[i])
        
        tmp = even_sum
        even_sum = 0

        for i in range(2, len(arr), 2):
            even_sum += len(ball_list[i])
        
        even_sum = min(tmp, even_sum)


        return min(odd_sum, even_sum)


print(solve(ball_list))
    