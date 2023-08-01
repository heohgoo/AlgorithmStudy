p, m = map(int, input().split())
rooms = []
visited = {}
dict = {}
cnt = 0

for _ in range(p):
    l = input()
    level, id = l.split()
    dict[id] = int(level)
    visited[id] = False


while True:
    tmp = []

    if cnt == p:
        break

    for key in dict:
        if len(tmp) == m:
            break
        if visited[key]:
            continue
        if not tmp:
            tmp.append(key)
            k = dict[key]
            visited[key] = True
            cnt += 1
        else:
            if k-10 <= dict[key] <= k+10:
                tmp.append(key)
                visited[key] = True
                cnt += 1
    rooms.append(tmp)

for room in rooms:
    room.sort()
    if len(room) == m:    
        print("Started!")
        for id in room:
            print(dict[id], end=" ")
            print(id)
    else:
        print("Waiting!")
        for id in room:
            print(dict[id], end=" ")
            print(id)