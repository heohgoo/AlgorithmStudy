n = int(input())
switch = [-1] + (list(map(int, input().split())))
m = int(input())
students = []

for _ in range(m):
    gender, num = map(int, input().split())
    students.append((gender, num))

def convert(num):
    if num == 1:
        return 0
    return 1

def male(idx):
    for i in range(1, (n//idx)+1):
        switch[idx*i] = convert(switch[idx*i])

def female(idx):
    switch[idx] = convert(switch[idx])

    if idx == n or idx == 1:
        return

    for i in range(1, min(idx-1, n-idx)+1):
        if switch[idx-i] != switch[idx+i]:
            break

        switch[idx-i] = convert(switch[idx-i])
        switch[idx+i] = convert(switch[idx+i]) 

for student in students:
    gender, num = student
    if gender == 1: #남학생
        male(num)
    else:
        female(num)

idx = 1

for i in range(1, n+1):
    print(switch[i], end=" ")
    if i == idx*20:
        print()
        idx += 1
