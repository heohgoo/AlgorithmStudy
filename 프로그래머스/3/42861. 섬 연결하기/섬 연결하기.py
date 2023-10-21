# #크루스칼
# def find_parent(parent, x):
#     if parent[x] != x: #부모 노드가 자신이 아닐 경우
#         find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a > b:
#         parent[a] = b
#     else:
#         parent[b] = a
    
# def solution(n, costs):
#     answer = 0
#     count = 0
#     parent = [i for i in range(n)]
#     costs.sort(key=lambda x:x[2])
    
#     for i in range(len(costs)):
#         a, b, cost = costs[i]
#         if find_parent(parent, a) != find_parent(parent, b):#두 노드의 부모 노드가 다를 경우(사이클x)
#             answer += cost
#             union_parent(parent, a, b)
#             count += 1
        
#         #연결선이 n-1개일 때가 최적이다.
#         if count == n-1:
#             break
    
#     return answer

# Union-Find Method
# get the  (smallest) parent node #
def getParent(parent, x):
    if parent[x] == x:
        return x
    return getParent(parent, parent[x])

# given two nodes to be connected, update their parents
def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# compare parent nodes of the given two nodes
# to see if they share the same parent - in this case, a cycle will be made
def compareParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a == b:
        return True
    else:
        return False

# main function
def solution(n, costs):
    answer = 0
    count = 0
    
    # initialize parent-node table
    parent = [0] * n
    for i in range(n):
        parent[i] = i
    
    # sort the costs table per cost
    costs.sort(key = lambda x: x[2])

    # if a edge does not make a cycle, add
    for x in costs:
        if not compareParent(parent,x[0], x[1]):
            answer += x[2]
            unionParent(parent, x[0],x[1])
            count += 1

        # if # of edges = n - 1, it's the best
        if count == n - 1:
            break

    return answer