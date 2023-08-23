#구현
n = int(input())
word = list(input())
word.sort()
word_dict = {}
answer = 0

for w in word:
    if w not in word_dict:
        word_dict[w] = 1
    else:
        word_dict[w] += 1


for _ in range(n-1):
    cp = list(input())
    cp_dict = {}
    cp.sort()

    for c in cp:
        if c not in cp_dict:
            cp_dict[c] = 1
        else:
            cp_dict[c] += 1
    
    if cp_dict == word_dict: # 같은 구성
        answer += 1
        continue

    if set(cp) == set(word): # 같은 문자로 구성
        if len(word)-1 <= len(cp) <= len(word)+1:
            answer += 1
            continue
    
    else:
        # 사본 생성
        tmp_word_dict = word_dict.copy()

        for c in cp_dict:
            if c in word_dict:
                if tmp_word_dict[c] > cp_dict[c]:
                    tmp_word_dict[c] -= cp_dict[c]
                    cp_dict[c] = 0
                else:
                    cp_dict[c] -= tmp_word_dict[c]
                    tmp_word_dict[c] = 0
                
        tmp_c, tmp_w = 0, 0

        for c in cp_dict:
            tmp_c += cp_dict[c]
        
        for w in tmp_word_dict:
            tmp_w += tmp_word_dict[w]
        
        if tmp_c <= 1 and tmp_w <= 1:
            answer += 1
            continue

print(answer)