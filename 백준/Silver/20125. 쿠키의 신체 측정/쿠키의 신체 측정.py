#추상화하면 더 좋을 듯?
n = int(input())
grid = []

for _ in range(n):
    row = list(input())
    grid.append(row)


def find_heart():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '*':
                heart = (i+1, j)
                return heart

def find_left_arm(h):
    x, y = h
    cnt = 0
    for i in range(y-1, -1, -1):
        if grid[x][i] != '*':
            return cnt
        else:
            cnt += 1
    return cnt


def find_right_arm(h):
    x, y = h
    cnt = 0
    for i in range(y+1, n):
        if grid[x][i] != '*':
            return cnt
        else:
            cnt += 1
    return cnt

def find_waist(h):
    x, y = h
    cnt = 0
    for i in range(x+1, n):
        if grid[i][y] != '*':
            return (i-1, y, cnt)
        else:
            cnt += 1

def find_left_leg(w):
    x, y = w
    cnt = 1
    x += 1
    y -= 1

    for i in range(x+1, n):
        if grid[i][y] != '*':
            return cnt
        else:
            cnt += 1
    return cnt
    

def find_right_leg(w):
    x, y = w
    cnt = 1
    x += 1
    y += 1

    for i in range(x+1, n):
        if grid[i][y] != '*':
            return cnt
        else:
            cnt += 1
    return cnt

heart = find_heart()
print(heart[0]+1, end=" ")
print(heart[1]+1)
print(find_left_arm(heart), end=" ")
print(find_right_arm(heart), end=" ")

wx, wy, waist = find_waist(heart)
print(waist, end=" ")

print(find_left_leg((wx, wy)), end=" ")
print(find_right_leg((wx, wy)), end=" ")
