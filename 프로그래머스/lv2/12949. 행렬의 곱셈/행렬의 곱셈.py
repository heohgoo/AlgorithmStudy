def solution(arr1, arr2):
    answer = []
    arr2_cv = [[0]*len(arr2) for _ in range(len(arr2[0]))]
    
    for i in range(len(arr2)):
        for j in range(len(arr2[0])):
            arr2_cv[j][i] = arr2[i][j]

    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2_cv)):
            tmp = 0
            for k in range(len(arr1[0])):
                tmp += arr1[i][k]*arr2_cv[j][k]
            row.append(tmp)
        answer.append(row)
                            
    return answer