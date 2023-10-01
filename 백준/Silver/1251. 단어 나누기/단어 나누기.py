word = list(input())
length = len(word)
#무조건 바꿔야 한다.
answer = 'z'*length

for first in range(length-2):
    for second in range(first+1, length-1):
        first_part = word[:first+1]
        first_part.reverse()
        second_part = word[first+1:second+1]
        second_part.reverse()        
        third_part = word[second+1:]
        third_part.reverse()  
        tmp = first_part + second_part + third_part  
        answer = min(answer, ''.join(tmp))
    
print(answer)