num = input()
cp = 0

while True:
    cp += 1
    tmp = str(cp)

    while len(tmp) > 0 and len(num) > 0:
        if tmp[0] == num[0]:
            num = num[1:]
        tmp = tmp[1:]

    if len(num) == 0:
        break

print(cp)