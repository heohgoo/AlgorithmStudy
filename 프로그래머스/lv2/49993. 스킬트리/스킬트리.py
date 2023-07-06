def solution(skill, skill_trees):
    cnt = 0
    skill = list(skill)
    
    for skill_tree in skill_trees:
        flag = True
        idx = 0
        skill_tree = list(skill_tree)
        for s in skill_tree:
            if s in skill:
                if s == skill[idx]:
                    idx += 1
                else:
                    flag = False
                    break
        
        if flag:
            cnt += 1
            
    return cnt