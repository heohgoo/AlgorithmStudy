n, k = map(int, input().split())

num_list = [i for i in range(1, n+1)]
ans = []

while num_list:
    idx = (k-1) % len(num_list)
    num_list = num_list[idx:] + num_list[:idx]
    ans.append(str(num_list.pop(0)))


print("<",", ".join(ans)[:],">", sep='')
# print('<', end='')
# for i in range(len(ans)):
#     if i != len(ans)-1:
#         print(ans[i], end=', ')
#     else:
#         print(ans[i], end='')
# print('>')
