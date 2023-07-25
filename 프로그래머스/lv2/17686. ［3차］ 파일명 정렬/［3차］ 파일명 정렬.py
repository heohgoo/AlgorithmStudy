def solution(files):
    answer = []
    info = []
    
    for idx, file in enumerate(files):
        info.append([idx, '', ''])
        flag = False
        
        for l in file:
            if l.isdigit():
                info[-1][2] += l
                flag = True
            
            else:
                if flag:
                    break
                info[-1][1] += l.lower()
        info[-1][2] = int(info[-1][2])
    
    info = sorted(info, key=lambda x:(x[1], x[2], x[0]))
    
    
    for i in range(len(info)):
        answer.append(files[info[i][0]])
                              
    return answer