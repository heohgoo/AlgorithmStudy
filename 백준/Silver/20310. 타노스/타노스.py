string = list(input())


def tanos(arr):
    zero = 0
    one = 0
    result = ''
    for i in range(len(arr)):
        if arr[i] == '0':
            zero += 1
        else:
            one += 1

    result += '0'*(zero//2)
    result += '1'*(one//2)
    return result
    

print(tanos(string))